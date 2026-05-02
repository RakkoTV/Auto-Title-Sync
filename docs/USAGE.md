# Usage Guide - Auto-Title-Sync

## Table of Contents
- [First Time Setup](#first-time-setup)
- [Configuring Twitch](#configuring-twitch)
- [Configuring YouTube](#configuring-youtube)
- [Creating Title Templates](#creating-title-templates)
- [Using Title Rotation](#using-title-rotation)
- [Advanced Features](#advanced-features)

## First Time Setup

### 1. Enable the Script

1. Open OBS Studio
2. Go to **Tools** → **Scripts**
3. Select `auto_title_sync.py`
4. Click **Script Settings**

### 2. Choose Your Language

Select from English, Spanish, Japanese, or Chinese for the interface.

## Configuring Twitch

### Step 1: Get Your Credentials

1. Go to [Twitch Dev Console](https://dev.twitch.tv/console)
2. Click **Register Your Application**
3. Fill in:
   - **Name**: `OBS Auto-Title-Sync`
   - **OAuth Redirect URL**: `http://localhost`
4. Click **Create**
5. Copy your **Client ID**

### Step 2: Get OAuth Token

1. In the Dev Console, click **Manage** on your app
2. Go to **Client ID** → **New Token**
3. Select scope: `channel:manage:broadcast`
4. Click **Generate Token**
5. Copy the token (save it securely!)

### Step 3: Get Channel ID

1. Go to https://www.twitchessel.com/
2. Enter your username
3. Copy your User ID

### Step 4: Configure in Script

In the script settings:
- **Enable Twitch**: ✅
- **Client ID**: Paste your Client ID
- **OAuth Token**: Paste your token
- **Channel ID**: Paste your User ID

## Configuring YouTube

### Step 1: Enable YouTube Data API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable **YouTube Data API v3**
4. Go to **Credentials** → **Create Credentials** → **OAuth Client ID**
5. Copy your **API Key**

### Step 2: Get Channel ID

1. Go to your YouTube channel
2. Copy the URL (e.g., `https://www.youtube.com/channel/UC...`)
3. The part after `channel/` is your Channel ID

### Step 3: Configure in Script

In the script settings:
- **Enable YouTube**: ✅
- **API Key**: Paste your API key
- **Channel ID**: Paste your Channel ID

## Creating Title Templates

### Template Placeholders

Use these placeholders in your titles:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{game}` | Current game/application | "Minecraft" |
| `{title}` | Stream title | "Chill Stream" |
| `{viewers}` | Current viewer count | "150" |
| `{time}` | Current time | "14:30" |

### Example Templates

**Gaming Template**:
```
Playing {game} | {viewers} viewers | !merch
```

**IRL Template**:
```
📍 IRL Stream | {time} | !socials
```

**Music Template**:
```
🎵 {title} | Request: {game}
```

## Using Title Rotation

### Enable Rotation

1. In script settings, enable **Rotate Titles**
2. Add multiple title templates
3. Set **Rotation Interval** (minutes)

### How It Works

- The script rotates through your titles every X minutes
- Great for showcasing different aspects of your stream
- Each platform (Twitch/YouTube) gets updated simultaneously

## Advanced Features

### Game Detection

When enabled:
- Script automatically detects the active window
- Updates `{game}` placeholder with window title
- Works with most games and applications

### Viewer Count Integration

When enabled:
- Fetches current viewer count
- Updates `{viewers}` placeholder in real-time
- Updates every refresh interval

### Hotkeys

- **Ctrl+Shift+T**: Update title immediately
- **Ctrl+Shift+N**: Next title template
- **Ctrl+Shift+P**: Previous title template

---

For more help, visit [GitHub Discussions](https://github.com/RakkoTV/Auto-Title-Sync/discussions)
