## 为什么做这个

我想要一个歌词工具，在 Windows、macOS 和 Linux 上都能用，既可以开成桌面窗口，也能放在终端或者状态栏里。OmniLyrics 的 Avalonia 图形界面、CLI 和 TUI 共用同一套 .NET 核心。

## 设计

- 五种 GUI 布局、双语卡拉 OK 歌词，偏好设置互通，还有队列缓存。
- CLI/TUI 界面，支持单行输出和 JSON 输出，方便接到状态栏和小组件上。
- 各平台的播放集成：Linux 上用 MPRIS，Windows 上用 SMTC，macOS 上原生接入 Apple Music / Spotify。
- 可以用脚本和快捷键控制播放。
- .NET 10 加 Avalonia。之前的项目里就用过 Avalonia，比较熟。

## 效果展示

现在的 Focus 布局：

![OmniLyrics 的 Focus 布局](images/omnilyrics-current.webp)

早期的 Windows GUI：

![Windows 上的 GUI](https://raw.githubusercontent.com/zzxzzk115/OmniLyrics/master/media/images/gui_windows.png)

Windows Terminal：

![Windows 上的 CLI](https://raw.githubusercontent.com/zzxzzk115/OmniLyrics/master/media/images/cli_windows_terminal.png)

Linux Waybar：

![Waybar 单行模式](https://raw.githubusercontent.com/zzxzzk115/OmniLyrics/master/media/images/cli_linux_waybar.jpg)

## 现状

目前的 README 对应的是 0.4.2 版，macOS 的 GUI 应用已经签名并通过了公证。GUI 和 CLI/TUI 分开下载，共用同一份偏好设置。便携版自带 .NET 运行时。

播放集成、布局和设置的说明见 [用户指南](https://github.com/zzxzzk115/OmniLyrics/blob/master/docs/user-guide.md)。
