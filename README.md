# Auto-Title-Sync for OBS Studio

Automatically update your stream title based on the game/application you're streaming, with multi-platform support for Twitch and YouTube.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OBS](https://img.shields.io/badge/OBS-28.0%2B-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Features

- **Auto-detect Game**: Automatically detects the current game/application window
- **Multi-platform**: Update titles on Twitch and YouTube simultaneously
- **Title Rotation**: Cycle through multiple titles on a schedule
- **Viewer Count**: Include current viewer count in title
- **Custom Templates**: Use placeholders like `{game}`, `{title}`, `{viewers}`, `{time}`
- **Multi-language UI**: English, Spanish, Japanese, Chinese
- **Hotkey Support**: Update title instantly with a hotkey

## Screenshots

![Auto-Title-Sync UI](https://img.shields.io/badge/UI-Settings-lightgrey)

## Installation

1. Download [`auto_title_sync.py`](auto_title_sync.py)
2. In OBS Studio, go to **Tools → Scripts**
3. Click the "+" button and select the downloaded file
4. Configure your credentials in the script properties

## Configuration

### Step 1: Get Twitch Credentials

1. Go to [Twitch Dev Console](https://dev.twitch.tv/console)
2. Create a new application
3. Copy your **Client ID**
4. Generate an **OAuth Token** with `channel:manage:broadcast` scope

### Step 2: Get YouTube Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create OAuth 2.0 credentials
3. Enable YouTube Data API v3
4. Copy your **API Key** and **Channel ID**

### Step 3: Configure Script

| Setting | Description | Default |
|---------|-------------|---------|
| Enable Twitch | Update Twitch stream title | Off |
| Client ID | Twitch application Client ID | - |
| OAuth Token | Twitch OAuth token with permissions | - |
| Channel ID | Your Twitch user ID | - |
| Enable YouTube | Update YouTube stream title | Off |
| Detect Game | Auto-detect current game/window | On |
| Include Viewers | Add viewer count to title | Off |
| Refresh Interval | How often to update (seconds) | 60 |
| Rotate Titles | Cycle through multiple titles | Off |
| Rotation Interval | Time between title rotations (minutes) | 30 |

### Title Templates

Use these placeholders in your titles:

- `{game}` - Current game/application name
- `{title}` - Original stream title
- `{viewers}` - Current viewer count
- `{time}` - Current time (HH:MM format)

Example: `Playing {game} | {viewers} viewers`

### Hotkeys

- **Ctrl+Shift+T** (default): Update stream title immediately

## Requirements

- **OBS Studio**: 28.0 or higher
- **Python**: 3.8 or higher (included with OBS)
- **Operating System**: Windows 10+, macOS 12+, Linux

## Troubleshooting

**Problem**: Script not appearing in OBS
- **Solution**: Make sure Python is installed and OBS is updated

**Problem**: Title not updating on Twitch
- **Solution**: Verify your OAuth token has `channel:manage:broadcast` scope

**Problem**: Game detection not working
- **Solution**: Game detection currently works on Windows only. Linux/macOS coming soon

## Changelog

### Version 1.0.0 (2026-05-01)
- Initial release
- Twitch and YouTube integration
- Auto game detection
- Title rotation
- Multi-language support

## Support

- Issues: [GitHub Issues](https://github.com/RakkoTV/Auto-Title-Sync/issues)
- Discussions: [GitHub Discussions](https://github.com/RakkoTV/Auto-Title-Sync/discussions)

## Donate

If you find this project useful, please consider supporting the development:

[![Donate](https://img.shields.io/badge/PayPal-Donate-blue)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)

**[Donate via PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)**

## Connect With Me

- **[GitHub](https://github.com/RakkoTV)** - ⭐ 3 Stars
- **[LinkedIn](https://www.linkedin.com/in/ramiro-silva/)** - 👥 449 Contacts
- **[Instagram](https://www.instagram.com/Rakko.Tech)** - 👥 6,666 Followers
- **[Twitch](https://www.twitch.tv/RakkoTech)** - 👥 8,800 Followers
- **[X/Twitter](https://www.x.com/RakkoTech)** - 👥 245 Followers

## License

This project is licensed under MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- OBS Studio team for the amazing streaming platform
- Twitch and YouTube API teams

---

Made with ❤️ by [RakkoTV](https://github.com/RakkoTV)
