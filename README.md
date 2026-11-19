# featured-projects

The project catalog behind [my homepage](https://zzxzzk115.github.io/) and [my blog](https://zzxzzk115.github.io/blog/).
Both sites read `catalog.json` from this repository when they build and render the same projects in their own way:
the homepage makes a card and a detail page for each project, the blog makes cards for its About page and its
column galleries (Porting, Software, Graphics & Engines).

## Layout

```
projects/<id>/
  project.yaml     metadata, fixed schema: schema/project.schema.json
  body.en.md       the homepage detail page (optional body.zh.md)
  images/          cover and images used in the body
schema/project.schema.json
scripts/build.py   validates every project.yaml and writes catalog.json
catalog.json       generated; what the sites read
```

## project.yaml

```yaml
id: vri                          # same as the folder name
order: 3                         # sort key in full lists
category: work                   # work | library | fun | indie | retro
tags: [C++23, RHI, Vulkan]
repo: zzxzzk115/VRI              # GitHub repo, for star counts (optional)
title: {en: VRI}
description:
  en: A cross-platform render hardware interface ...
  zh: 跨平台渲染硬件接口 ...
status: {en: In development, zh: 开发中}
image: {src: images/vri.webp, alt: {en: ...}, fit: cover}
links:
  - {label: {en: Source, zh: 源码}, href: https://github.com/zzxzzk115/VRI, icon: brands:github}
overview: {en: {purpose: ..., contribution: ..., outcome: ...}}
homepage:                        # on the homepage (needs body.en.md)
  path: /projects/vri/
  modes: [academic, casual]
  home: {academic: {order: 3}}   # featured on the home page, or false
blog:
  about: true                    # in the full list on the blog's About page
  columns: {graphics: 3}         # in these column galleries, at this position
```

Reader-facing text is `{en: ..., zh: ...}`; Chinese is optional and falls back to English. A link's `href` can be one
address or `{en: ..., zh: ...}`.

## Editing

```bash
pip install pyyaml jsonschema
python scripts/build.py          # after editing: validates and rewrites catalog.json
```

Commit `catalog.json` with your change; CI fails if it is out of date. After a push to `main`, CI asks both sites to
rebuild when the `SITES_DISPATCH_TOKEN` secret is set (a fine-grained token with Contents read/write on
`zzxzzk115/zzxzzk115.github.io` and `zzxzzk115/blog`); otherwise they pick the change up on their next build.
