#!/bin/bash

# Job Tracker - Local Application Tracker
# Startup script for Mac/Linux

echo ""
echo "==============================================="
echo "   Job Tracker - Local Application Tracker"
echo "==============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Error: Python is not installed."
        echo "   Please install Python 3.7+ from https://python.org"
        echo "   On macOS: brew install python"
        echo "   On Ubuntu/Debian: sudo apt install python3 python3-pip"
        read -p "Press Enter to exit..."
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ Python found: $($PYTHON_CMD --version)"
echo ""

# Check Python version
python_version=$($PYTHON_CMD -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.7"

if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]]; then
    echo "❌ Error: Python 3.7 or higher is required."
    echo "   Current version: $python_version"
    read -p "Press Enter to exit..."
    exit 1
fi

# Install requirements
echo "📦 Installing/checking requirements..."
$PYTHON_CMD -m pip install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    echo "❌ Error installing requirements."
    echo "   Please check your internet connection and try again."
    echo "   You may need to run: sudo $PYTHON_CMD -m pip install -r requirements.txt"
    read -p "Press Enter to exit..."
    exit 1
fi

echo "✅ Requirements installed"
echo ""

# Create directories
mkdir -p data uploads
echo "📁 Directories prepared"
echo ""

# Check for clipboard utilities on Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v xsel &> /dev/null && ! command -v xclip &> /dev/null; then
        echo "⚠️  Warning: Clipboard utilities not found."
        echo "   Install for better clipboard monitoring:"
        echo "   sudo apt-get install xsel xclip"
        echo ""
    fi
fi

# Start the application
echo "🚀 Starting Job Tracker..."
echo "📋 Clipboard monitoring will be active!"
echo "🌐 Opening browser at http://127.0.0.1:5000"
echo ""
echo "==============================================="
echo "           🎯 JOB TRACKER IS RUNNING"
echo "==============================================="
echo "✅ Copy any job URL to create a draft application"
echo "🔗 Visit http://127.0.0.1:5000 if browser doesn't open"
echo "⏹️  Press Ctrl+C to stop the server"
echo "==============================================="
echo ""

# Set trap to handle Ctrl+C gracefully
trap 'echo -e "\n👋 Job Tracker stopped."; exit 0' INT

$PYTHON_CMD app.py

echo ""
echo "👋 Job Tracker stopped."