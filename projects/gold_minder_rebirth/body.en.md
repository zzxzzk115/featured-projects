[View repository ↗](https://github.com/zzxzzk115/GoldMiner-Rebirth)

<iframe frameborder="0" src="https://itch.io/embed/1548293" width="552" height="167" title="Gold Miner Rebirth preview" loading="lazy"><a href="https://lazy-v.itch.io/goldminer-rebirth">GoldMiner-Rebirth by Lazy_V</a></iframe>

## Why This Exists

My friends and I loved this Flash game as kids, so I decided to bring it back — not as a reinterpretation, but as a faithful recreation, running on the retro gaming handhelds I collect: GameShell, Trimui Smart Pro and Brick. Other ports depend on a compatible LÖVE runtime and device-specific testing.

## Design Notes

**Why LÖVE2D?** I originally started on raylib, but on the GameShell it was unstable — even texture loading could fail. LÖVE 11.1 ran reliably on the handheld, so I switched, and LÖVE provides a shared runtime for the handheld ports; each target still needs platform-specific testing.

**Keeping it authentic.** The most fun part of the project was learning to **unpack the original `.swf` file** — extracting the ActionScript and the original asset files. That's what makes the remake taste like the original: same art, same feel, not a lookalike.
