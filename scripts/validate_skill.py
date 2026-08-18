#!/usr/bin/env python3
"""
Standalone validator for SKILL.md.

Checks the things that actually break a skill on upload or on load:
  - SKILL.md exists
  - YAML frontmatter parses (a bare colon in an unquoted description is the
    classic way this breaks, which is exactly what happened during this
    skill's own development)
  - required fields (name, description) are present and non-empty
  - the body isn't absurdly long, a soft warning, not a failure

Exits 0 and prints "OK" on success, exits 1 and prints the problem on failure.
Run from the repo root: python scripts/validate_skill.py
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml")
    sys.exit(1)

REQUIRED_FIELDS = ["name", "description"]
LINE_COUNT_WARNING = 500


def validate(skill_md_path: Path) -> tuple[bool, str]:
    if not skill_md_path.exists():
        return False, f"{skill_md_path} not found"

    text = skill_md_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return False, "SKILL.md must start with a --- YAML frontmatter block"

    parts = text.split("---", 2)
    if len(parts) < 3:
        return False, "Could not find a closing --- for the frontmatter block"

    frontmatter_raw = parts[1]
    body = parts[2]

    try:
        frontmatter = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    if not isinstance(frontmatter, dict):
        return False, "Frontmatter must be a YAML mapping (key: value pairs)"

    missing = [f for f in REQUIRED_FIELDS if not frontmatter.get(f)]
    if missing:
        return False, f"Missing or empty required field(s): {', '.join(missing)}"

    line_count = len(body.splitlines())
    warning = ""
    if line_count > LINE_COUNT_WARNING:
        warning = (
            f" (warning: body is {line_count} lines, consider splitting into "
            f"references/ if it keeps growing)"
        )

    return True, f"SKILL.md is valid{warning}"


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    ok, message = validate(repo_root / "SKILL.md")
    print(message)
    sys.exit(0 if ok else 1)
