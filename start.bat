@echo off
title Job Tracker - Local Application Tracker

echo.
echo ===============================================
echo    Job Tracker - Local Application Tracker
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH.
    echo    Please install Python 3.7+ from https://python.org
    echo    Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Install requirements
echo 📦 Installing/checking requirements...
python -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ❌ Error installing requirements.
    echo    Please check your internet connection and try again.
    pause
    exit /b 1
)

echo ✅ Requirements installed
echo.

REM Create directories
if not exist "data" mkdir data
if not exist "uploads" mkdir uploads
echo 📁 Directories prepared
echo.

REM Start the application
echo 🚀 Starting Job Tracker...
echo 📋 Clipboard monitoring will be active!
echo 🌐 Opening browser at http://127.0.0.1:5000
echo.
echo ===============================================
echo           🎯 JOB TRACKER IS RUNNING
echo ===============================================
echo ✅ Copy any job URL to create a draft application
echo 🔗 Visit http://127.0.0.1:5000 if browser doesn't open
echo ⏹️  Press Ctrl+C to stop the server
echo ===============================================
echo.

python app.py

echo.
echo 👋 Job Tracker stopped.
pause