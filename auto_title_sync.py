#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-Title-Sync for OBS Studio
Automatically update stream title based on game/application
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from typing import Optional, Dict, List

try:
    import obspython
except ImportError:
    print("This script must be run within OBS Studio")
    sys.exit(1)


# =============================================================================
# INTERNATIONALIZATION STRINGS
# =============================================================================

I18N = {
    "en": {
        "script_name": "Auto-Title-Sync",
        "script_description": "Automatically update stream title based on game/application",
        "tab_settings": "Settings",
        "tab_titles": "Title Templates",
        "tab_advanced": "Advanced",
        "group_twitch": "Twitch Settings",
        "group_youtube": "YouTube Settings",
        "group_general": "General Settings",
        "label_client_id": "Client ID",
        "label_client_secret": "Client Secret",
        "label_token": "OAuth Token",
        "label_channel": "Channel ID",
        "label_refresh_interval": "Refresh Interval (seconds)",
        "label_enable_twitch": "Enable Twitch",
        "label_enable_youtube": "Enable YouTube",
        "label_title_template": "Title Template",
        "label_add_title": "Add Title",
        "label_remove_title": "Remove",
        "label_detect_game": "Auto-detect Game",
        "label_include_viewers": "Include Viewer Count",
        "label_rotate_titles": "Rotate Titles",
        "label_rotation_interval": "Rotation Interval (minutes)",
        "label_test_connection": "Test Connection",
        "label_update_now": "Update Now",
        "success_connection": "Connection successful!",
        "error_connection": "Connection failed: {}",
        "error_missing_credentials": "Missing credentials",
        "info_title_updated": "Title updated: {}",
        "info_game_detected": "Game detected: {}",
        "help_placeholder": "{game} = current game, {title} = stream title, {viewers} = viewer count"
    },
    "es": {
        "script_name": "Auto-Title-Sync",
        "script_description": "Actualizar automáticamente el título del stream basado en el juego/aplicación",
        "tab_settings": "Configuración",
        "tab_titles": "Plantillas de Título",
        "tab_advanced": "Avanzado",
        "group_twitch": "Configuración de Twitch",
        "group_youtube": "Configuración de YouTube",
        "group_general": "Configuración General",
        "label_client_id": "ID de Cliente",
        "label_client_secret": "Secreto de Cliente",
        "label_token": "Token OAuth",
        "label_channel": "ID del Canal",
        "label_refresh_interval": "Intervalo de Actualización (segundos)",
        "label_enable_twitch": "Habilitar Twitch",
        "label_enable_youtube": "Habilitar YouTube",
        "label_title_template": "Plantilla de Título",
        "label_add_title": "Agregar Título",
        "label_remove_title": "Eliminar",
        "label_detect_game": "Detectar Juego Automáticamente",
        "label_include_viewers": "Incluir Contador de Espectadores",
        "label_rotate_titles": "Rotar Títulos",
        "label_rotation_interval": "Intervalo de Rotación (minutos)",
        "label_test_connection": "Probar Conexión",
        "label_update_now": "Actualizar Ahora",
        "success_connection": "¡Conexión exitosa!",
        "error_connection": "Conexión fallida: {}",
        "error_missing_credentials": "Credenciales faltantes",
        "info_title_updated": "Título actualizado: {}",
        "info_game_detected": "Juego detectado: {}",
        "help_placeholder": "{game} = juego actual, {title} = título del stream, {viewers} = espectadores"
    },
    "jp": {
        "script_name": "Auto-Title-Sync",
        "script_description": "ゲーム/アプリケーションに基づいてストリームタイトルを自動更新",
        "tab_settings": "設定",
        "tab_titles": "タイトルテンプレート",
        "tab_advanced": "詳細",
        "group_twitch": "Twitch設定",
        "group_youtube": "YouTube設定",
        "group_general": "一般設定",
        "label_client_id": "クライアントID",
        "label_client_secret": "クライアントシークレット",
        "label_token": "OAuthトークン",
        "label_channel": "チャンネルID",
        "label_refresh_interval": "更新間隔（秒）",
        "label_enable_twitch": "Twitchを有効化",
        "label_enable_youtube": "YouTubeを有効化",
        "label_title_template": "タイトルテンプレート",
        "label_add_title": "タイトルを追加",
        "label_remove_title": "削除",
        "label_detect_game": "ゲームを自動検出",
        "label_include_viewers": "視聴者数を含める",
        "label_rotate_titles": "タイトルをローテート",
        "label_rotation_interval": "ローテート間隔（分）",
        "label_test_connection": "接続テスト",
        "label_update_now": "今すぐ更新",
        "success_connection": "接続に成功しました！",
        "error_connection": "接続に失敗しました: {}",
        "error_missing_credentials": "認証情報が不足しています",
        "info_title_updated": "タイトルを更新しました: {}",
        "info_game_detected": "ゲームを検出しました: {}",
        "help_placeholder": "{game} = 現在のゲーム, {title} = ストリームタイトル, {viewers} = 視聴者数"
    },
    "cn": {
        "script_name": "Auto-Title-Sync",
        "script_description": "根据游戏/应用程序自动更新直播标题",
        "tab_settings": "设置",
        "tab_titles": "标题模板",
        "tab_advanced": "高级",
        "group_twitch": "Twitch设置",
        "group_youtube": "YouTube设置",
        "group_general": "常规设置",
        "label_client_id": "客户端ID",
        "label_client_secret": "客户端密钥",
        "label_token": "OAuth令牌",
        "label_channel": "频道ID",
        "label_refresh_interval": "刷新间隔（秒）",
        "label_enable_twitch": "启用Twitch",
        "label_enable_youtube": "启用YouTube",
        "label_title_template": "标题模板",
        "label_add_title": "添加标题",
        "label_remove_title": "删除",
        "label_detect_game": "自动检测游戏",
        "label_include_viewers": "包含观看人数",
        "label_rotate_titles": "轮换标题",
        "label_rotation_interval": "轮换间隔（分钟）",
        "label_test_connection": "测试连接",
        "label_update_now": "立即更新",
        "success_connection": "连接成功！",
        "error_connection": "连接失败: {}",
        "error_missing_credentials": "缺少凭据",
        "info_title_updated": "标题已更新: {}",
        "info_game_detected": "检测到游戏: {}",
        "help_placeholder": "{game} = 当前游戏, {title} = 直播标题, {viewers} = 观看人数"
    }
}


def t(key: str, lang: str = "en", **kwargs) -> str:
    """Get translated string"""
    if lang not in I18N:
        lang = "en"
    keys = key.split(".")
    value = I18N[lang]
    for k in keys:
        value = value.get(k, key)
    if kwargs:
        try:
            return value.format(**kwargs)
        except (KeyError, ValueError):
            return value
    return value


# =============================================================================
# SCRIPT STATE
# =============================================================================

class ScriptState:
    def __init__(self):
        self.language = "en"
        self.twitch_enabled = False
        self.twitch_client_id = ""
        self.twitch_client_secret = ""
        self.twitch_token = ""
        self.twitch_channel = ""
        self.youtube_enabled = False
        self.youtube_token = ""
        self.youtube_channel = ""
        self.refresh_interval = 60
        self.title_templates = []
        self.detect_game = True
        self.include_viewers = False
        self.rotate_titles = False
        self.rotation_interval = 30
        self.current_title_index = 0
        self.last_rotation_time = 0
        self.current_game = ""
        self.current_viewers = 0
        self.timer = None
        self.hotkey_update = None

    def save(self, settings):
        """Save settings to OBS data"""
        obspython.obs_data_set_bool(settings, "twitch_enabled", self.twitch_enabled)
        obspython.obs_data_set_string(settings, "twitch_client_id", self.twitch_client_id)
        obspython.obs_data_set_string(settings, "twitch_client_secret", self.twitch_client_secret)
        obspython.obs_data_set_string(settings, "twitch_token", self.twitch_token)
        obspython.obs_data_set_string(settings, "twitch_channel", self.twitch_channel)
        obspython.obs_data_set_bool(settings, "youtube_enabled", self.youtube_enabled)
        obspython.obs_data_set_string(settings, "youtube_token", self.youtube_token)
        obspython.obs_data_set_string(settings, "youtube_channel", self.youtube_channel)
        obspython.obs_data_set_int(settings, "refresh_interval", self.refresh_interval)
        obspython.obs_data_set_bool(settings, "detect_game", self.detect_game)
        obspython.obs_data_set_bool(settings, "include_viewers", self.include_viewers)
        obspython.obs_data_set_bool(settings, "rotate_titles", self.rotate_titles)
        obspython.obs_data_set_int(settings, "rotation_interval", self.rotation_interval)
        obspython.obs_data_set_int(settings, "language", ["en", "es", "jp", "cn"].index(self.language))

        # Save title templates as JSON array
        titles_json = json.dumps(self.title_templates)
        obspython.obs_data_set_string(settings, "title_templates", titles_json)

    def load(self, settings):
        """Load settings from OBS data"""
        self.twitch_enabled = obspython.obs_data_get_bool(settings, "twitch_enabled", False)
        self.twitch_client_id = obspython.obs_data_get_string(settings, "twitch_client_id") or ""
        self.twitch_client_secret = obspython.obs_data_get_string(settings, "twitch_client_secret") or ""
        self.twitch_token = obspython.obs_data_get_string(settings, "twitch_token") or ""
        self.twitch_channel = obspython.obs_data_get_string(settings, "twitch_channel") or ""
        self.youtube_enabled = obspython.obs_data_get_bool(settings, "youtube_enabled", False)
        self.youtube_token = obspython.obs_data_get_string(settings, "youtube_token") or ""
        self.youtube_channel = obspython.obs_data_get_string(settings, "youtube_channel") or ""
        self.refresh_interval = obspython.obs_data_get_int(settings, "refresh_interval", 60)
        self.detect_game = obspython.obs_data_get_bool(settings, "detect_game", True)
        self.include_viewers = obspython.obs_data_get_bool(settings, "include_viewers", False)
        self.rotate_titles = obspython.obs_data_get_bool(settings, "rotate_titles", False)
        self.rotation_interval = obspython.obs_data_get_int(settings, "rotation_interval", 30)

        lang_idx = obspython.obs_data_get_int(settings, "language", 0)
        self.language = ["en", "es", "jp", "cn"][lang_idx] if 0 <= lang_idx < 4 else "en"

        # Load title templates from JSON
        titles_json = obspython.obs_data_get_string(settings, "title_templates") or "[]"
        try:
            self.title_templates = json.loads(titles_json)
        except json.JSONDecodeError:
            self.title_templates = []


# Global state
state = ScriptState()


# =============================================================================
# API HELPERS
# =============================================================================

def make_api_request(url: str, headers: Dict[str, str], data: Optional[bytes] = None) -> Optional[Dict]:
    """Make HTTP API request"""
    try:
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        obspython.script_log(obspython.LOG_WARNING, f"HTTP Error: {e.code}")
        return None
    except urllib.error.URLError as e:
        obspython.script_log(obspython.LOG_WARNING, f"URL Error: {e.reason}")
        return None
    except Exception as e:
        obspython.script_log(obspython.LOG_WARNING, f"Request Error: {str(e)}")
        return None


def update_twitch_title(title: str) -> bool:
    """Update Twitch stream title"""
    if not state.twitch_enabled or not state.twitch_token or not state.twitch_channel:
        return False

    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={state.twitch_channel}"
    headers = {
        "Client-ID": state.twitch_client_id,
        "Authorization": f"Bearer {state.twitch_token}",
        "Content-Type": "application/json"
    }
    data = json.dumps({"title": title}).encode('utf-8')

    result = make_api_request(url, headers, data)
    return result is not None


def update_youtube_title(title: str) -> bool:
    """Update YouTube stream title"""
    if not state.youtube_enabled or not state.youtube_token or not state.youtube_channel:
        return False

    # YouTube API requires more complex setup
    # This is a simplified version
    url = f"https://www.googleapis.com/youtube/v3/liveBroadcasts?part=snippet&id={state.youtube_channel}"
    headers = {
        "Authorization": f"Bearer {state.youtube_token}",
        "Content-Type": "application/json"
    }

    # Get current broadcast data first
    result = make_api_request(url, headers)
    if result and "items" in result and len(result["items"]) > 0:
        snippet = result["items"][0]["snippet"]
        snippet["title"] = title

        # Update the broadcast
        data = json.dumps({"snippet": snippet, "id": state.youtube_channel}).encode('utf-8')
        update_result = make_api_request(url, headers, data)
        return update_result is not None

    return False


def get_current_window() -> str:
    """Get current focused window title (game detection)"""
    try:
        if sys.platform == "win32":
            import win32gui
            window = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(window)
        elif sys.platform == "darwin":
            # macOS implementation would go here
            pass
        elif sys.platform.startswith("linux"):
            # Linux implementation would go here
            pass
    except ImportError:
        obspython.script_log(obspython.LOG_WARNING, "Window detection not available")
    except Exception as e:
        obspython.script_log(obspython.LOG_WARNING, f"Window detection error: {str(e)}")
    return ""


def get_viewer_count() -> int:
    """Get current viewer count from Twitch/YouTube"""
    viewers = 0

    if state.twitch_enabled and state.twitch_token and state.twitch_channel:
        url = f"https://api.twitch.tv/helix/streams?user_id={state.twitch_channel}"
        headers = {
            "Client-ID": state.twitch_client_id,
            "Authorization": f"Bearer {state.twitch_token}"
        }
        result = make_api_request(url, headers)
        if result and "data" in result and len(result["data"]) > 0:
            viewers = result["data"][0].get("viewer_count", 0)

    return viewers


# =============================================================================
# TITLE MANAGEMENT
# =============================================================================

def format_title(template: str) -> str:
    """Format title template with current values"""
    title = template
    title = title.replace("{game}", state.current_game)
    title = title.replace("{title}", state.title_templates[0] if state.title_templates else "")
    title = title.replace("{viewers}", str(state.current_viewers))
    title = title.replace("{time}", datetime.now().strftime("%H:%M"))
    return title


def get_current_title() -> str:
    """Get current title to use"""
    if not state.title_templates:
        return f"Streaming {state.current_game}"

    if state.rotate_titles and len(state.title_templates) > 1:
        current_time = time.time()
        if current_time - state.last_rotation_time >= state.rotation_interval * 60:
            state.current_title_index = (state.current_title_index + 1) % len(state.title_templates)
            state.last_rotation_time = current_time

    return format_title(state.title_templates[state.current_title_index])


def update_stream_title():
    """Update stream title on all platforms"""
    # Detect current game/window
    if state.detect_game:
        window = get_current_window()
        if window:
            state.current_game = window

    # Get viewer count
    if state.include_viewers:
        state.current_viewers = get_viewer_count()

    # Get formatted title
    title = get_current_title()

    # Update platforms
    success = False
    if state.twitch_enabled:
        if update_twitch_title(title):
            success = True
            obspython.script_log(obspython.LOG_INFO, t("info_title_updated", state.language, title=title))

    if state.youtube_enabled:
        if update_youtube_title(title):
            success = True
            obspython.script_log(obspython.LOG_INFO, t("info_title_updated", state.language, title=title))

    return success


# =============================================================================
# TIMER CALLBACK
# =============================================================================

def timer_callback UNUSED:
    """Timer callback for periodic updates"""
    UNUSED = None
    update_stream_title()


def start_timer():
    """Start the update timer"""
    if state.timer:
        obspython.timer_remove(state.timer)

    if state.refresh_interval > 0:
        state.timer = obspython.timer_add(state.refresh_interval * 1000, timer_callback)


def stop_timer():
    """Stop the update timer"""
    if state.timer:
        obspython.timer_remove(state.timer)
        state.timer = None


# =============================================================================
# HOTKEY CALLBACK
# =============================================================================

def hotkey_update_callback UNUSED:
    """Hotkey callback to update title immediately"""
    UNUSED = None
    update_stream_title()


# =============================================================================
# UI CALLBACKS
# =============================================================================

def on_update_clicked(props, prop UNUSED, UNUSED2):
    """Update now button clicked"""
    UNUSED = None
    UNUSED2 = None
    update_stream_title()


def on_test_clicked(props, prop UNUSED, UNUSED2):
    """Test connection button clicked"""
    UNUSED = None
    UNUSED2 = None

    # Test Twitch connection
    if state.twitch_enabled and state.twitch_token:
        url = "https://api.twitch.tv/helix/users"
        headers = {
            "Client-ID": state.twitch_client_id,
            "Authorization": f"Bearer {state.twitch_token}"
        }
        result = make_api_request(url, headers)
        if result:
            obspython.script_log(obspython.LOG_INFO, t("success_connection", state.language))
        else:
            obspython.script_log(obspython.LOG_ERROR, t("error_connection", state.language, error="Twitch"))


def on_language_changed(props, prop, data):
    """Language selection changed"""
    lang_idx = obspython.obs_data_get_int(data, "language")
    state.language = ["en", "es", "jp", "cn"][lang_idx]
    obspython.obs_properties_refresh(props)


# =============================================================================
# OBS SCRIPT PROPERTIES
# =============================================================================

def script_properties():
    """Create script properties panel"""
    props = obspython.obs_properties_create()

    # Language selection
    lang_list = obspython.obs_property_list_add
    lang = obspython.obs_properties_add_list(props, "language", "Language", obspython.OBS_COMBO_TYPE_LIST, obspython.OBS_COMBO_FORMAT_INT)
    lang_list(lang, "English", 0)
    lang_list(lang, "Español", 1)
    lang_list(lang, "日本語", 2)
    lang_list(lang, "中文", 3)
    obspython.obs_property_set_modified_callback(lang, on_language_changed)

    # General Settings
    general = obspython.obs_properties_create()
    obspython.obs_properties_add_group(props, "general_group", t("group_general", state.language), obspython.OBS_GROUP_NORMAL, general)

    obspython.obs_properties_add_bool(general, "detect_game", t("label_detect_game", state.language))
    obspython.obs_properties_add_bool(general, "include_viewers", t("label_include_viewers", state.language))
    obspython.obs_properties_add_int(general, "refresh_interval", t("label_refresh_interval", state.language), 10, 3600, 10)

    # Title Rotation
    rotation = obspython.obs_properties_create()
    obspython.obs_properties_add_group(general, "rotation_group", t("label_rotate_titles", state.language), obspython.OBS_GROUP_CHECKABLE, rotation)

    obspython.obs_properties_add_int(rotation, "rotation_interval", t("label_rotation_interval", state.language), 1, 120, 1)

    # Twitch Settings
    twitch = obspython.obs_properties_create()
    obspython.obs_properties_add_group(props, "twitch_group", t("group_twitch", state.language), obspython.OBS_GROUP_NORMAL, twitch)

    obspython.obs_properties_add_bool(twitch, "twitch_enabled", t("label_enable_twitch", state.language))
    obspython.obs_properties_add_text(twitch, "twitch_client_id", t("label_client_id", state.language), obspython.OBS_TEXT_DEFAULT)
    obspython.obs_properties_add_text(twitch, "twitch_token", t("label_token", state.language), obspython.OBS_TEXT_PASSWORD)
    obspython.obs_properties_add_text(twitch, "twitch_channel", t("label_channel", state.language), obspython.OBS_TEXT_DEFAULT)

    # YouTube Settings
    youtube = obspython.obs_properties_create()
    obspython.obs_properties_add_group(props, "youtube_group", t("group_youtube", state.language), obspython.OBS_GROUP_NORMAL, youtube)

    obspython.obs_properties_add_bool(youtube, "youtube_enabled", t("label_enable_youtube", state.language))
    obspython.obs_properties_add_text(youtube, "youtube_token", t("label_token", state.language), obspython.OBS_TEXT_PASSWORD)
    obspython.obs_properties_add_text(youtube, "youtube_channel", t("label_channel", state.language), obspython.OBS_TEXT_DEFAULT)

    # Action Buttons
    obspython.obs_properties_add_button(props, "update_now", t("label_update_now", state.language), on_update_clicked)
    obspython.obs_properties_add_button(props, "test_connection", t("label_test_connection", state.language), on_test_clicked)

    return props


def script_update(settings):
    """Settings updated callback"""
    state.load(settings)
    start_timer()


def script_save(settings):
    """Save settings callback"""
    state.save(settings)


def script_load(settings):
    """Load settings callback"""
    state.load(settings)

    # Register hotkey
    state.hotkey_update = obspython.obs_hotkey_register_frontend(
        "auto_title_sync.update",
        "Update Stream Title",
        hotkey_update_callback,
        None
    )

    start_timer()


def script_unload():
    """Unload script callback"""
    stop_timer()

    if state.hotkey_update:
        obspython.obs_hotkey_unregister(state.hotkey_update)


def script_description():
    """Script description for OBS"""
    return t("script_description", state.language)


def script_name():
    """Script name for OBS"""
    return "Auto-Title-Sync by RakkoTV"
