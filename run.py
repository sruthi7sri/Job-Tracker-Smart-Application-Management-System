#!/usr/bin/env python3
"""
Job Tracker - Easy Start Script
Run this script to start the Job Tracker application with proper error handling.
"""

import sys
import subprocess
import os
import webbrowser
import time
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"   Current version: {sys.version}")
        print("   Please upgrade Python and try again.")
        return False
    return True

def install_requirements():
    """Install required packages if not already installed."""
    requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print("❌ Error: requirements.txt file not found.")
        print("   Make sure you're running this script from the job-tracker directory.")
        return False
    
    print("📦 Checking/Installing requirements...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"
        ])
        print("✅ Requirements installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        print("   Try running: pip install -r requirements.txt")
        return False

def check_directories():
    """Create necessary directories."""
    directories = ["data", "uploads"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("📁 Directories prepared.")

def start_application():
    """Start the Flask application."""
    app_file = Path("app.py")
    
    if not app_file.exists():
        print("❌ Error: app.py file not found.")
        print("   Make sure you're running this script from the job-tracker directory.")
        return False
    
    print("🚀 Starting Job Tracker...")
    print("📋 Clipboard monitoring will be active!")
    print("🌐 Opening browser at http://127.0.0.1:5000")
    print("\n" + "="*50)
    print("🎯 JOB TRACKER IS RUNNING")
    print("="*50)
    print("✅ Copy any job URL to create a draft application")
    print("🔗 Visit http://127.0.0.1:5000 if browser doesn't open")
    print("⏹️  Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    
    try:
        # Import and run the Flask app
        import app
        return True
    except ImportError as e:
        print(f"❌ Error importing app: {e}")
        print("   Make sure all requirements are installed.")
        return False
    except KeyboardInterrupt:
        print("\n👋 Job Tracker stopped by user.")
        return True
    except Exception as e:
        print(f"❌ Error running application: {e}")
        return False

def main():
    """Main execution function."""
    print("🎯 Job Tracker - Local Application Tracker")
    print("=========================================\n")
    
    # Check Python version
    if not check_python_version():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check directories
    check_directories()
    
    # Start application
    if not start_application():
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)