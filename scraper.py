#!/usr/bin/env python3
"""
Ethical Web Scraper for Job Tracker
Respects robots.txt, implements rate limiting, and includes error handling.
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
import re
from typing import Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EthicalJobScraper:
    def __init__(self):
        self.session = requests.Session()
        # Set a respectful user agent
        self.session.headers.update({
            'User-Agent': 'Job-Tracker/1.0 (Educational Project; Contact: your-email@example.com)'
        })
        
        # Rate limiting: minimum seconds between requests
        self.min_delay = 2
        self.max_delay = 5
        self.last_request_time = 0
        
        # Cache for robots.txt checks
        self.robots_cache = {}
    
    def can_fetch(self, url: str) -> bool:
        """Check if we're allowed to fetch this URL according to robots.txt"""
        try:
            parsed_url = urlparse(url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            
            if base_url not in self.robots_cache:
                robots_url = urljoin(base_url, '/robots.txt')
                rp = RobotFileParser()
                rp.set_url(robots_url)
                try:
                    rp.read()
                    self.robots_cache[base_url] = rp
                except:
                    # If robots.txt can't be read, be conservative
                    logger.warning(f"Could not read robots.txt for {base_url}")
                    return False
            
            return self.robots_cache[base_url].can_fetch('*', url)
        except:
            return False
    
    def rate_limit(self):
        """Implement respectful rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_delay:
            sleep_time = random.uniform(self.min_delay, self.max_delay)
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def safe_request(self, url: str) -> Optional[requests.Response]:
        """Make a safe, rate-limited request"""
        try:
            # Check robots.txt first
            if not self.can_fetch(url):
                logger.warning(f"Robots.txt disallows fetching {url}")
                return None
            
            # Rate limiting
            self.rate_limit()
            
            # Make request with timeout
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            logger.info(f"Successfully fetched {url}")
            return response
            
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def scrape_job_info(self, url: str) -> Dict[str, str]:
        """
        Scrape job information from a URL.
        Only works for sites that allow it and have simple HTML structure.
        """
        
        # Default response
        result = {
            'company': '',
            'role': '',
            'location': '',
            'salary': '',
            'description': '',
            'error': None
        }
        
        response = self.safe_request(url)
        if not response:
            result['error'] = "Could not fetch page or robots.txt disallows"
            return result
        
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try to extract information based on common patterns
            # Note: These selectors are generic and may not work for all sites
            
            # Company name
            company_selectors = [
                'h1[data-company]', '.company-name', '.employer-name',
                'span[itemprop="hiringOrganization"]', '.job-company',
                'a[data-company-name]'
            ]
            
            for selector in company_selectors:
                element = soup.select_one(selector)
                if element:
                    result['company'] = element.get_text().strip()
                    break
            
            # Job title
            title_selectors = [
                'h1.job-title', 'h1[data-job-title]', '.job-title',
                'span[itemprop="title"]', '.position-title',
                'h1.jobsearch-JobInfoHeader-title'
            ]
            
            for selector in title_selectors:
                element = soup.select_one(selector)
                if element:
                    result['role'] = element.get_text().strip()
                    break
            
            # Location
            location_selectors = [
                'span[itemprop="jobLocation"]', '.job-location',
                '.location', '[data-job-location]'
            ]
            
            for selector in location_selectors:
                element = soup.select_one(selector)
                if element:
                    result['location'] = element.get_text().strip()
                    break
            
            # Salary (if available)
            salary_selectors = [
                'span[itemprop="baseSalary"]', '.salary',
                '.compensation', '[data-salary]'
            ]
            
            for selector in salary_selectors:
                element = soup.select_one(selector)
                if element:
                    result['salary'] = element.get_text().strip()
                    break
            
            logger.info(f"Successfully scraped job info from {url}")
            
        except Exception as e:
            result['error'] = f"Error parsing HTML: {str(e)}"
            logger.error(f"Error parsing {url}: {e}")
        
        return result
    
    def scrape_company_careers(self, url: str) -> Dict[str, str]:
        """
        Scrape from company career pages (more likely to allow scraping)
        """
        result = {
            'company': '',
            'role': '',
            'location': '',
            'salary': '',
            'error': None
        }
        
        response = self.safe_request(url)
        if not response:
            result['error'] = "Could not fetch page or robots.txt disallows"
            return result
        
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract company from URL or page title
            parsed_url = urlparse(url)
            domain_parts = parsed_url.netloc.split('.')
            if len(domain_parts) >= 2:
                # Try to get company name from domain
                company_name = domain_parts[-2]  # e.g., 'google' from 'careers.google.com'
                result['company'] = company_name.capitalize()
            
            # Look for job title in common locations
            title_element = (
                soup.find('h1') or 
                soup.find('title') or
                soup.select_one('.job-title, .position-title, .role-title')
            )
            
            if title_element:
                title_text = title_element.get_text().strip()
                # Clean up title (remove common prefixes/suffixes)
                title_text = re.sub(r'^(Job:|Position:|Role:)\s*', '', title_text, flags=re.IGNORECASE)
                title_text = re.sub(r'\s*-\s*.*$', '', title_text)  # Remove everything after dash
                result['role'] = title_text
            
            logger.info(f"Successfully scraped company career page: {url}")
            
        except Exception as e:
            result['error'] = f"Error parsing HTML: {str(e)}"
            logger.error(f"Error parsing {url}: {e}")
        
        return result

# Integration with existing job tracker
def enhance_job_info_with_scraping(url: str, existing_info: Dict[str, str]) -> Dict[str, str]:
    """
    Enhance existing URL-parsed info with scraped data where appropriate
    """
    scraper = EthicalJobScraper()
    
    # Only attempt scraping on company career pages or sites known to allow it
    allowed_patterns = [
        r'.*\.careers\..*',
        r'.*careers\..*',
        r'.*jobs\..*',
        r'.*greenhouse\.io.*',  # Some Greenhouse sites allow it
    ]
    
    should_scrape = any(re.match(pattern, url, re.IGNORECASE) for pattern in allowed_patterns)
    
    if not should_scrape:
        logger.info(f"Skipping scraping for {url} - not on allowlist")
        return existing_info
    
    # Try scraping
    if 'greenhouse.io' in url:
        scraped_info = scraper.scrape_job_info(url)
    else:
        scraped_info = scraper.scrape_company_careers(url)
    
    # Merge scraped info with existing info (existing takes precedence)
    enhanced_info = existing_info.copy()
    
    for key, value in scraped_info.items():
        if key != 'error' and value and not enhanced_info.get(key):
            enhanced_info[key] = value
    
    if scraped_info.get('error'):
        logger.warning(f"Scraping error for {url}: {scraped_info['error']}")
    
    return enhanced_info

# Usage example
if __name__ == "__main__":
    # Test with a hypothetical company career page
    scraper = EthicalJobScraper()
    
    # This would only work if the site allows scraping
    test_url = "https://example-company.com/careers/software-engineer"
    result = scraper.scrape_company_careers(test_url)
    print(result)