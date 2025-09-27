# Job Tracker - Smart Application Management System

A privacy-focused job application tracking system that automates data entry and provides powerful analytics for job seekers.

## Features

### Core Functionality
- **Local SQLite Database** - All data stored securely on your machine
- **Smart URL Detection** - Automatically detects job URLs from 15+ platforms
- **Real-time Status Updates** - Update application statuses without page refreshes
- **Excel Integration** - Import existing spreadsheets and export your data
- **Follow-up Management** - Never miss important follow-up dates

### Intelligent Automation
- **Clipboard Monitoring** - Auto-creates application drafts when you copy job URLs
- **Platform Recognition** - Supports LinkedIn, Greenhouse, Lever, Workday, Indeed, AngelList, and more
- **Data Extraction** - Automatically extracts company names, job IDs, and platform information from URLs
- **Draft Review System** - Review and edit auto-generated entries before saving

### Advanced Analytics
- **Sankey Flow Diagrams** - Visualize your job search funnel from applications to offers
- **Success Metrics** - Track response rates, interview conversion, and offer rates  
- **Platform Performance** - Identify which job boards work best for you
- **Timeline Analysis** - See your application activity patterns over time
- **Smart Insights** - Get personalized recommendations based on your data

### Organization Tools
- **11 Status Types** - From "Applied" to "Accepted" with everything in between
- **Tagging System** - Organize applications by company type, role, location, etc.
- **Advanced Search** - Find applications quickly by company or role name
- **Status Filtering** - Filter by Applied, Interview, Offers, Rejected, etc.
- **Comprehensive Notes** - Track interview feedback, salary negotiations, and more

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/job-tracker.git
cd job-tracker

# Install dependencies
pip install Flask pyperclip openpyxl

# Create required directories
mkdir data uploads

# Run the application
python app.py
```

Open your browser to `http://127.0.0.1:5000`

## How It Works

### 1. Automatic URL Detection
Copy any job URL from supported platforms:
```
https://linkedin.com/jobs/view/12345
https://company.greenhouse.io/jobs/67890
https://jobs.lever.co/company/position-name
```

### 2. Smart Data Extraction
The system automatically extracts:
- **Company name** (from URL patterns)
- **Job ID** (from URL parameters) 
- **Platform** (LinkedIn, Greenhouse, etc.)
- **Application date** (today's date)

### 3. Review and Save
A modal popup appears with pre-filled information. Add the job title and any additional details, then save.

### 4. Track and Analyze
Use the dashboard to:
- Update application statuses
- View your application pipeline
- Analyze success patterns
- Get follow-up reminders

## Supported Platforms

| Platform | Company Extraction | Job ID Extraction | Notes |
|----------|-------------------|-------------------|--------|
| LinkedIn | ❌ | ✅ | Manual company entry required |
| Greenhouse | ✅ | ✅ | From subdomain pattern |
| Lever | ✅ | ❌ | From URL path |
| Workday | ✅ | ❌ | From URL path |
| Indeed | ❌ | ❌ | Platform detection only |
| AngelList | ❌ | ❌ | Platform detection only |
| Company Sites | ❌ | ❌ | Platform detection only |

## Screenshots

### Dashboard
![Dashboard showing application list with status updates and statistics]

### Analytics
![Sankey diagram showing job application flow from applications to offers]

### Add Application
![Form with auto-filled fields from clipboard monitoring]

*Screenshots coming soon - add actual images to showcase the interface*

## Tech Stack

**Backend:**
- Python 3.7+
- Flask web framework
- SQLite database
- Threading for background processing

**Frontend:**
- Bootstrap 5 for responsive UI
- Vanilla JavaScript for interactivity
- Plotly.js for data visualizations
- Bootstrap Icons

**Key Libraries:**
- `pyperclip` - Clipboard monitoring
- `openpyxl` - Excel file processing
- `flask` - Web framework
- No pandas dependency for Python 3.12+ compatibility

## Data Schema

```sql
CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    job_id TEXT,
    date_applied DATE DEFAULT CURRENT_DATE,
    status TEXT DEFAULT 'Applied',
    url TEXT UNIQUE,
    platform TEXT,
    location TEXT,
    salary TEXT,
    notes TEXT,
    tags TEXT,
    next_action TEXT,
    follow_up_on DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Privacy & Security

- **100% Local** - No cloud services or external APIs required
- **No Tracking** - No telemetry, analytics, or data collection
- **Offline Capable** - Works completely offline after initial setup
- **Your Data** - Complete control over your job search information
- **Open Source** - Transparent code you can audit and modify

## Installation Options

### Option 1: Direct Installation
```bash
pip install Flask pyperclip openpyxl
python app.py
```

### Option 2: Virtual Environment (Recommended)
```bash
python3 -m venv job-tracker-env
source job-tracker-env/bin/activate  # On Windows: job-tracker-env\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Option 3: Using Startup Scripts
**Windows:**
```bash
# Double-click start.bat
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

## Usage Tips

### Maximize Automation
1. Keep the application running while job searching
2. Copy job URLs directly from job sites
3. Review auto-filled information before saving
4. Use tags consistently for better filtering

### Analytics Insights
- Check your response rate to optimize application strategy
- Identify which platforms work best for your field
- Track seasonal application patterns
- Monitor follow-up effectiveness

### Data Management
- Export to Excel monthly for backup
- Use tags like "remote", "startup", "big-tech" for organization  
- Set follow-up dates 1-2 weeks after applying
- Keep detailed notes for interview preparation

## System Requirements

- **Python:** 3.7 or higher (tested on 3.12)
- **Storage:** ~50MB for application and data
- **Memory:** ~100MB RAM during operation
- **Browser:** Any modern web browser
- **OS:** Windows, macOS, Linux

### Platform-Specific Notes

**macOS:**
- May require clipboard access permissions
- Use `python3` command

**Windows:**  
- Security warnings for clipboard access are normal
- Use `python` command

**Linux:**
- Install clipboard utilities: `sudo apt-get install xsel xclip`

## Troubleshooting

### Common Issues

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**Port 5000 in use:**
```bash
# Change port in app.py or kill existing process
lsof -ti:5000 | xargs kill -9
```

**Clipboard monitoring not working:**
- Grant clipboard permissions when prompted
- On Linux, install xsel or xclip
- Restart application after permission changes

**Database errors:**
```bash
# Check permissions
ls -la data/
# Recreate database
rm data/jobtracker.sqlite3
python app.py
```

## Contributing

This project demonstrates production-ready development practices:

### Development Standards
- Clean, documented code
- Error handling and input validation
- Cross-platform compatibility
- Security-conscious design

### Future Enhancements
- [ ] Email integration for automatic status updates
- [ ] Machine learning for success prediction
- [ ] Mobile companion app
- [ ] Team collaboration features
- [ ] Advanced reporting and exports
- [ ] Integration with job board APIs

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

Having issues? Check the troubleshooting section above or:

1. Verify system requirements
2. Check file permissions in `data/` directory  
3. Test with a fresh virtual environment
4. Review browser console for JavaScript errors

Built for job seekers who value privacy and want data-driven insights into their application process.

---

**Star this repo if it helps with your job search!**