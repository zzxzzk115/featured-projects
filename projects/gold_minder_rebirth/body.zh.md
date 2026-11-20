[查看仓库 ↗](https://github.com/zzxzzk115/GoldMiner-Rebirth)

<iframe frameborder="0" src="https://itch.io/embed/1548293" width="552" height="167" title="Gold Miner Rebirth preview" loading="lazy"><a href="https://lazy-v.itch.io/goldminer-rebirth">GoldMiner-Rebirth by Lazy_V</a></iframe>

## 为什么做它

小时候我和朋友们都很喜欢这个 Flash 游戏，所以我决定把它找回来。不是重新诠释，而是原汁原味地还原，让它跑在我收藏的几台复古掌机上：GameShell、Trimui Smart Pro 和 Brick。其他平台的移植要看有没有兼容的 LÖVE 运行时，也得在具体设备上测试。

## 设计笔记

**为什么用 LÖVE2D？** 我一开始用的是 raylib，但它在 GameShell 上不稳定，连加载纹理都可能失败。LÖVE 11.1 在这台掌机上跑得很稳，于是我就换了过来。LÖVE 给各个掌机移植版提供了一套共用的运行时，不过每个平台还是要单独测试。

**保持原味。** 整个项目里最好玩的部分，是学着 **拆开原版的 `.swf` 文件**，把里面的 ActionScript 和原始素材文件提取出来。正因为这样，重制版吃起来才是原来的味道：一样的美术，一样的手感，而不是长得像而已。
