[查看仓库 ↗](https://github.com/SnowLeopardEngine/SnowLeopardEngine)

<iframe width="100%" height="600" src="https://www.youtube.com/embed/z9oA2pugC6s?si=rY38cth64wPILTV_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen loading="lazy"></iframe>

## 为什么做它

Snow Leopard Engine 是利兹大学 **High-Performance Graphics and Games Engineering**（高性能图形与游戏工程）硕士专业的小组课程项目（COMP5530M，2023/24）：从零写一个游戏引擎，再在它上面做一个游戏 demo 来证明它能用，也就是上面视频里的那个 demo。

## 小组成员

| 姓名                                             | 负责内容                                                             |
| ------------------------------------------------ | -------------------------------------------------------------------- |
| [Kexuan Zhang](https://zzxzzk115.github.io/)     | 组长。架构、核心系统、渲染、编辑器、音频、报告                       |
| Ziyu Min                                         | 副组长。渲染、Shader、报告                                           |
| Jubiao Lin                                       | 物理、游戏内 GUI、海报                                               |
| [Simiao Wang](https://wangsimiao2000.github.io/) | 物理、海报、展示视频                                                 |
| Ruofan He                                        | 玩法（寻路）                                                         |
| [Haodong Lin](https://leolanger.github.io/)      | 动画                                                                 |
| Yanni Ma                                         | 编辑器                                                               |

## 我们做了什么

- 基于现代 OpenGL 4.6 的渲染器，支持 PBR 和后处理效果
- **DzShader**：一种类似 Unity、数据驱动的 shader 格式。这是我第一次尝试数据驱动的 shader 写法，这个想法后来慢慢成熟，变成了 [vshadersystem](/projects/vultra_ecosystem/#vshadersystem)。
- PhysX 物理模拟、骨骼动画、简单的游戏内 GUI，还有一个编辑器
- 尝试过接入 **C# 脚本**（构建依赖里已经有 .NET SDK 了），但 API 绑定最后没做完。后来 native / Lua / C# 脚本方面的工作，记录在 [libvultra 目前的开发分支](https://github.com/zzxzzk115/libvultra/tree/dev-VRI) 里。

## 回顾

最大的收获是人：七个队友，每个人都有自己擅长的东西。最大的遗憾是时间：课业和考试都在抢大家的时间，我作为组长要把项目撑下去，压力扛了不少。最后没能做到我期望的完成度，不过交出来的东西还算拿得出手。

这些遗憾也没有白费。整体式、OpenGL 时代的引擎有哪些不足，加上想把它真正做好的念头，正是 [Vultra Ecosystem](/projects/vultra_ecosystem/) 的起点。

## 许可证

MIT，详见 [仓库](https://github.com/SnowLeopardEngine/SnowLeopardEngine/blob/main/LICENSE)。
