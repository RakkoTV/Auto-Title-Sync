# OBS Studio 自动标题同步

根据您正在直播的游戏/应用程序自动更新直播标题，支持 Twitch 和 YouTube 多平台。

![版本](https://img.shields.io/badge/版本-1.0.0-blue)
![许可证](https://img.shields.io/badge/许可证-MIT-green)
![OBS](https://img.shields.io/badge/OBS-28.0%2B-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## 功能特点

- **自动检测游戏**: 自动检测当前游戏/应用程序窗口
- **多平台支持**: 同时在 Twitch 和 YouTube 更新标题
- **标题轮换**: 按计划循环显示多个标题
- **观众数量**: 在标题中包含当前观众数量
- **自定义模板**: 使用占位符如 `{game}`、`{title}`、`{viewers}`、`{time}`
- **多语言界面**: 英语、西班牙语、日语、中文
- **快捷键支持**: 使用快捷键立即更新标题

## 安装

1. 下载 [`auto_title_sync.py`](auto_title_sync.py)
2. 在 OBS Studio 中，转到**工具 → 脚本**
3. 点击"+"按钮并选择下载的文件
4. 在脚本属性中配置您的凭据

## 配置

### 步骤 1: 获取 Twitch 凭据

1. 前往 [Twitch 开发者控制台](https://dev.twitch.tv/console)
2. 创建新应用程序
3. 复制您的**客户端 ID**
4. 生成具有 `channel:manage:broadcast` 范围的 **OAuth 令牌**

### 步骤 2: 获取 YouTube 凭据

1. 前往 [Google Cloud 控制台](https://console.cloud.google.com/)
2. 创建 OAuth 2.0 凭据
3. 启用 YouTube Data API v3
4. 复制您的**API 密钥**和**频道 ID**

### 步骤 3: 配置脚本

| 设置 | 描述 | 默认值 |
|------|------|--------|
| 启用 Twitch | 更新 Twitch 直播标题 | 关闭 |
| 客户端 ID | Twitch 应用程序客户端 ID | - |
| OAuth 令牌 | 具有权限的 Twitch OAuth 令牌 | - |
| 频道 ID | 您的 Twitch 用户 ID | - |
| 启用 YouTube | 更新 YouTube 直播标题 | 关闭 |
| 检测游戏 | 自动检测当前游戏/窗口 | 开启 |
| 包含观众数量 | 将观众数量添加到标题 | 关闭 |
| 刷新间隔 | 更新频率（秒） | 60 |
| 轮换标题 | 在多个标题之间循环 | 关闭 |
| 轮换间隔 | 标题轮换之间的时间（分钟） | 30 |

### 标题模板

在标题中使用这些占位符：

- `{game}` - 当前游戏/应用程序名称
- `{title}` - 原始直播标题
- `{viewers}` - 当前观众数量
- `{time}` - 当前时间（HH:MM 格式）

示例: `正在玩 {game} | {viewers} 位观众`

### 快捷键

- **Ctrl+Shift+T**（默认）: 立即更新直播标题

## 系统要求

- **OBS Studio**: 28.0 或更高版本
- **Python**: 3.8 或更高版本（包含在 OBS 中）
- **操作系统**: Windows 10+、macOS 12+、Linux

## 故障排除

**问题**: 脚本未在 OBS 中显示
- **解决方案**: 确保已安装 Python 并已更新 OBS

**问题**: Twitch 上的标题未更新
- **解决方案**: 验证您的 OAuth 令牌具有 `channel:manage:broadcast` 范围

**问题**: 游戏检测不工作
- **解决方案**: 游戏检测目前仅在 Windows 上有效。Linux/macOS 即将推出

## 更新日志

### 版本 1.0.0 (2026-05-01)
- 首次发布
- Twitch 和 YouTube 集成
- 自动游戏检测
- 标题轮换
- 多语言支持

## 支持

- 问题反馈: [GitHub Issues](https://github.com/RakkoTV/Auto-Title-Sync/issues)
- 讨论区: [GitHub Discussions](https://github.com/RakkoTV/Auto-Title-Sync/discussions)

## 捐赠

如果您觉得这个项目有用，请考虑支持开发：

[![捐赠](https://img.shields.io/badge/PayPal-捐赠-blue)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)

**[通过 PayPal 捐赠](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)**

## 与我联系

- **[GitHub](https://github.com/RakkoTV)** - ⭐ 3 星
- **[领英](https://www.linkedin.com/in/ramiro-silva/)** - 👥 449 位联系人
- **[Instagram](https://www.instagram.com/Rakko.Tech)** - 👥 6,666 位关注者
- **[Twitch](https://www.twitch.tv/RakkoTech)** - 👥 8,800 位关注者
- **[X/推特](https://www.x.com/RakkoTech)** - 👥 245 位关注者

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE)

## 致谢

- OBS Studio 团队提供的惊人流媒体平台
- Twitch 和 YouTube API 团队

---

由 [RakkoTV](https://github.com/RakkoTV) 用 ❤️ 制作
