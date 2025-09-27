#!/usr/bin/env python3
"""
Configuration for web scraping functionality
"""

# Web scraping settings
SCRAPING_CONFIG = {
    # Enable/disable web scraping globally
    'ENABLED': True,
    
    # Rate limiting (seconds between requests)
    'MIN_DELAY': 2,
    'MAX_DELAY': 5,
    
    # Request timeout (seconds)
    'TIMEOUT': 10,
    
    # User agent string
    'USER_AGENT': 'Job-Tracker/1.0 (Educational Project; Contact: your-email@example.com)',
    
    # Sites where scraping is likely acceptable (company career pages)
    'ALLOWED_PATTERNS': [
        r'.*careers\..*',
        r'.*jobs\..*',
        r'.*\.careers\..*',
        r'.*hire\..*',
        r'.*work\..*',
        # Add more patterns as needed
    ],
    
    # Sites to never scrape (respect their ToS)
    'BLOCKED_DOMAINS': [
        'linkedin.com',
        'indeed.com',
        'glassdoor.com',
        # Add more as needed
    ],
    
    # CSS selectors for common job information
    'SELECTORS': {
        'job_title': [
            'h1.job-title',
            'h1[data-job-title]',
            '.job-title',
            'h1.position-title',
            '.position-title',
            '.role-title',
            'h1:first-of-type'
        ],
        'company': [
            '.company-name',
            '.employer-name',
            '[data-company]',
            '.company',
            '.employer'
        ],
        'location': [
            '.job-location',
            '.location',
            '[data-location]',
            '.job-location-text',
            '.position-location'
        ],
        'salary': [
            '.salary',
            '.compensation',
            '[data-salary]',
            '.salary-range',
            '.pay-range'
        ]
    }
}

# Legal disclaimer
LEGAL_DISCLAIMER = """
Web scraping functionality is provided for educational purposes only.
Users are responsible for:
1. Respecting website Terms of Service
2. Checking robots.txt files
3. Implementing appropriate rate limiting
4. Obtaining permission when required

This tool implements best practices but cannot guarantee legal compliance
for all use cases. Use at your own discretion and risk.
"""