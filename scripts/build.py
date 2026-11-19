"""Validate projects/*/project.yaml and write catalog.json, the file the sites read.

    pip install pyyaml jsonschema
    python scripts/build.py           # validate and write catalog.json (CI runs this and commits the result)
    python scripts/build.py --check   # validate and fail if catalog.json is out of date

catalog.json: {"schemaVersion": 1, "projects": [...]} sorted by order then id. Each project is its project.yaml
with image paths made repo-relative ("projects/<id>/images/x.webp"), plus "body": {"en": "...", "zh": "..."} from
body.en.md / body.zh.md (image references inside rewritten the same way).
"""
import json, re, sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "project.schema.json").read_text(encoding="utf-8"))
OUT = ROOT / "catalog.json"


def main():
    check = "--check" in sys.argv
    validator = Draft202012Validator(SCHEMA)
    errors, projects = [], []
    for d in sorted(p for p in (ROOT / "projects").iterdir() if p.is_dir()):
        f = d / "project.yaml"
        if not f.exists():
            errors.append(f"{d.name}: no project.yaml")
            continue
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        for e in validator.iter_errors(data):
            errors.append(f"{d.name}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
        if data.get("id") != d.name:
            errors.append(f"{d.name}: id {data.get('id')!r} does not match the folder name")
        prefix = f"projects/{d.name}/"
        img = data.get("image")
        if img:
            if not (d / img["src"]).exists():
                errors.append(f"{d.name}: image {img['src']} not found")
            img["src"] = prefix + img["src"]
        body = {}
        for lang in ("en", "zh"):
            b = d / f"body.{lang}.md"
            if b.exists():
                text = b.read_text(encoding="utf-8")
                for ref in re.findall(r"(?<![\w/.])images/[^\s)\"']+", text):
                    if not (d / ref).exists():
                        errors.append(f"{d.name}: body.{lang}.md references missing {ref}")
                body[lang] = re.sub(r"(?<![\w/.])images/", prefix + "images/", text)
        if data.get("homepage") and "en" not in body:
            errors.append(f"{d.name}: on the homepage but has no body.en.md")
        if body:
            data["body"] = body
        projects.append(data)
    ids = [p["id"] for p in projects]
    for col in ("porting", "software", "graphics", "game-dev"):
        pos = [(p["blog"]["columns"][col], p["id"]) for p in projects if col in (p.get("blog") or {}).get("columns", {})]
        dup = {n for n, _ in pos if [x for x, _ in pos].count(n) > 1}
        if dup:
            errors.append(f"blog column {col}: duplicate positions {sorted(dup)}")
    if len(set(ids)) != len(ids):
        errors.append("duplicate ids")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    projects.sort(key=lambda p: (p["order"], p["id"]))
    text = json.dumps({"schemaVersion": 1, "projects": projects}, ensure_ascii=False, indent=1) + "\n"
    if check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            sys.exit("catalog.json is out of date: run python scripts/build.py and commit it")
        print(f"ok: {len(projects)} projects, catalog.json up to date")
        return
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote catalog.json: {len(projects)} projects")


if __name__ == "__main__":
    main()
