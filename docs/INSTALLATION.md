# Installation Guide - Auto-Title-Sync

## Table of Contents
- [Prerequisites](#prerequisites)
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Verifying Installation](#verifying-installation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- **OBS Studio**: Version 28.0 or higher
- **Python**: Version 3.8 or higher (usually included with OBS)
- **Internet Connection**: Required for Twitch/YouTube API access

## Windows Installation

### Step 1: Download the Script

1. Go to [Releases](https://github.com/RakkoTV/Auto-Title-Sync/releases)
2. Download `auto_title_sync.py`
3. Save it to a memorable location (e.g., `Documents/OBS Scripts/`)

### Step 2: Add to OBS Studio

1. Open OBS Studio
2. Go to **Tools** → **Scripts**
3. Click the **+** button
4. Navigate to and select `auto_title_sync.py`
5. Click **Open**

### Step 3: Configure

1. With the script selected, click **Script Settings**
2. Choose your language
3. Configure your Twitch/YouTube credentials
4. Set up title templates
5. Click **Apply**

## macOS Installation

### Step 1: Download the Script

1. Go to [Releases](https://github.com/RakkoTV/Auto-Title-Sync/releases)
2. Download `auto_title_sync.py`
3. Save it to `~/Documents/OBS Scripts/`

### Step 2: Add to OBS Studio

1. Open OBS Studio
2. Go to **Tools** → **Scripts**
3. Click the **+** button
4. Navigate to and select `auto_title_sync.py`
5. Click **Open**

## Linux Installation

### Step 1: Download the Script

```bash
wget https://github.com/RakkoTV/Auto-Title-Sync/releases/download/v1.0.0/auto_title_sync.py
```

### Step 2: Add to OBS Studio

1. Open OBS Studio
2. Go to **Tools** → **Scripts**
3. Click the **+** button
4. Navigate to and select `auto_title_sync.py`
5. Click **Open**

## Verifying Installation

After installation, verify:

1. ✅ Script appears in the Scripts list
2. ✅ No error messages in the Script Log
3. ✅ Settings panel opens when script is selected
4. ✅ Script shows as "Loaded" in status

## Troubleshooting

### Script Not Appearing

**Problem**: Script doesn't show in OBS Scripts list

**Solutions**:
- Verify OBS Studio is version 28.0 or higher
- Check that Python is installed (OBS Studio → Help → Log Files → Check for Python errors)
- Try moving the script to a different location

### Module Import Errors

**Problem**: "Module 'obspython' not found"

**Solutions**:
- Make sure you're running the script from within OBS Studio
- Do not run the script directly with Python

### Connection Errors

**Problem**: "Failed to connect to Twitch/YouTube"

**Solutions**:
- Verify your OAuth token has correct permissions
- Check your internet connection
- Ensure Client ID and Channel ID are correct

---

For more help, visit [GitHub Issues](https://github.com/RakkoTV/Auto-Title-Sync/issues)
