# OBS Studio 用 Auto-Title-Sync

配信中のゲーム/アプリケーションに基づいて自動的に配信タイトルを更新します。TwitchとYouTubeのマルチプラットフォーム対応。

![バージョン](https://img.shields.io/badge/バージョン-1.0.0-blue)
![ライセンス](https://img.shields.io/badge/ライセンス-MIT-green)
![OBS](https://img.shields.io/badge/OBS-28.0%2B-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## 特徴

- **自動ゲーム検出**: 現在のゲーム/アプリケーションウィンドウを自動検出
- **マルチプラットフォーム**: TwitchとYouTubeで同時にタイトルを更新
- **タイトルローテーション**: スケジュールに従って複数のタイトルを循環
- **視聴者数表示**: タイトルに現在の視聴者数を含める
- **カスタムテンプレート**: `{game}`、`{title}`、`{viewers}`、`{time}`などのプレースホルダーを使用
- **マルチ言語UI**: 英語、スペイン語、日本語、中国語
- **ホットキーサポート**: ホットキーでタイトルを即座に更新

## インストール

1. [`auto_title_sync.py`](auto_title_sync.py)をダウンロード
2. OBS Studioで**ツール → スクリプト**に移動
3. 「+」ボタンをクリックしてダウンロードしたファイルを選択
4. スクリプトプロパティで認証情報を設定

## 設定

### ステップ 1: Twitchの認証情報を取得

1. [Twitch開発者コンソール](https://dev.twitch.tv/console)に移動
2. 新しいアプリケーションを作成
3. **クライアントID**をコピー
4. `channel:manage:broadcast`スコープで**OAuthトークン**を生成

### ステップ 2: YouTubeの認証情報を取得

1. [Google Cloud Console](https://console.cloud.google.com/)に移動
2. OAuth 2.0認証情報を作成
3. YouTube Data API v3を有効化
4. **APIキー**と**チャンネルID**をコピー

### ステップ 3: スクリプトを設定

| 設定 | 説明 | デフォルト |
|------|------|-----------|
| Twitchを有効化 | Twitch配信タイトルを更新 | オフ |
| クライアントID | TwitchアプリケーションのクライアントID | - |
| OAuthトークン | 権限を持つTwitch OAuthトークン | - |
| チャンネルID | TwitchユーザーID | - |
| YouTubeを有効化 | YouTube配信タイトルを更新 | オフ |
| ゲームを検出 | 現在のゲーム/ウィンドウを自動検出 | オン |
| 視聴者数を含める | タイトルに視聴者数を追加 | オフ |
| 更新間隔 | 更新頻度（秒） | 60 |
| タイトルをローテート | 複数のタイトルを循環 | オフ |
| ローテーション間隔 | タイトルローテーションの間隔（分） | 30 |

### タイトルテンプレート

タイトルでこれらのプレースホルダーを使用：

- `{game}` - 現在のゲーム/アプリケーション名
- `{title}` - 元の配信タイトル
- `{viewers}` - 現在の視聴者数
- `{time}` - 現在時刻（HH:MM形式）

例: `{game}をプレイ中 | {viewers}人の視聴者`

### ホットキー

- **Ctrl+Shift+T**（デフォルト）: 配信タイトルを即座に更新

## 動作環境

- **OBS Studio**: 28.0以降
- **Python**: 3.8以降（OBSに含まれています）
- **オペレーティングシステム**: Windows 10+、macOS 12+、Linux

## トラブルシューティング

**問題**: スクリプトがOBSに表示されない
- **解決策**: Pythonがインストールされ、OBSが更新されていることを確認してください

**問題**: Twitchでタイトルが更新されない
- **解決策**: OAuthトークンに`channel:manage:broadcast`スコープがあることを確認してください

**問題**: ゲーム検出が機能しない
- **解決策**: ゲーム検出は現在Windowsのみで動作します。Linux/macOSは近日公開予定

## 更新履歴

### バージョン 1.0.0 (2026-05-01)
- 初回リリース
- TwitchとYouTubeの統合
- 自動ゲーム検出
- タイトルローテーション
- マルチ言語サポート

## サポート

- Issues: [GitHub Issues](https://github.com/RakkoTV/Auto-Title-Sync/issues)
- Discussions: [GitHub Discussions](https://github.com/RakkoTV/Auto-Title-Sync/discussions)

## 寄付

このプロジェクトが役に立った場合は、開発をサポートすることをご検討ください：

[![寄付](https://img.shields.io/badge/PayPal-寄付-blue)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)

**[PayPalで寄付する](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&currency_code=USD)**

## 私とつながる

- **[GitHub](https://github.com/RakkoTV)** - ⭐ 3スター
- **[LinkedIn](https://www.linkedin.com/in/ramiro-silva/)** - 👥 449人の連絡先
- **[Instagram](https://www.instagram.com/Rakko.Tech)** - 👥 6,666人のフォロワー
- **[Twitch](https://www.twitch.tv/RakkoTech)** - 👥 8,800人のフォロワー
- **[X/Twitter](https://www.x.com/RakkoTech)** - 👥 245人のフォロワー

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細は[LICENSE](LICENSE)を参照してください

## 謝辞

- 素晴らしいストリーミングプラットフォームを提供してくれたOBS Studioチーム
- TwitchとYouTube APIチーム

---

[RakkoTV](https://github.com/RakkoTV)が ❤️ で作成
