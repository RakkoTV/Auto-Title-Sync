# Troubleshooting - Auto-Title-Sync

## Common Issues and Solutions

### Connection Issues

#### "Failed to connect to Twitch"

**Causes**:
- Invalid OAuth token
- Incorrect Client ID
- Network issues

**Solutions**:
1. Verify your token at https://www.twitchsingular.com/
2. Check token has `channel:manage:broadcast` scope
3. Test token: `curl -H "Authorization: Bearer <token>" https://api.twitch.tv/helix/users`
4. Regenerate token if expired

#### "Failed to connect to YouTube"

**Causes**:
- Invalid API key
- YouTube Data API not enabled
- Quota exceeded

**Solutions**:
1. Verify API key in Google Cloud Console
2. Enable YouTube Data API v3
3. Check quota usage
4. Try again after quota reset (Pacific time)

### Title Not Updating

#### Title updates but doesn't show on Twitch

**Causes**:
- Stream not live
- Rate limiting
- Incorrect channel ID

**Solutions**:
1. Make sure you're live streaming
2. Wait 60 seconds between updates
3. Verify your Twitch User ID

#### Title updates but doesn't show on YouTube

**Causes**:
- Incorrect channel ID format
- API not enabled
- Privacy settings

**Solutions**:
1. Use channel ID format: `UCxxxxxxxxxxxxxxxxxx`
2. Enable YouTube Data API v3
3. Check channel is public

### Script Errors

#### "Module 'obspython' has no attribute 'timer_add'"

**Causes**:
- OBS version too old
- Python compatibility issue

**Solutions**:
1. Update OBS Studio to latest version
2. Reinstall OBS Studio with Python included

#### Script fails to load

**Causes**:
- Syntax error in script file
- Missing dependencies
- File encoding issues

**Solutions**:
1. Redownload the script
2. Check Script Log (Help → Log Files → Show Script Logs)
3. Verify file encoding is UTF-8

### Platform-Specific Issues

#### Windows: Game detection not working

**Causes**:
- Administrator privileges required
- Game running in different session

**Solutions**:
1. Run OBS Studio as Administrator
2. Run game in same user session

#### macOS: Script not appearing

**Causes**:
- Gatekeeper blocking
- Python path issues

**Solutions**:
1. Right-click OBS → Open
2. Install Python 3.8+ from python.org
3. Reinstall OBS Studio

#### Linux: Script errors

**Causes**:
- Missing Python packages
- OBS built without Python support

**Solutions**:
1. Install python3-obspython package
2. Rebuild OBS with Python enabled

---

Still having issues? [Create an issue on GitHub](https://github.com/RakkoTV/Auto-Title-Sync/issues)
