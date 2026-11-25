#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt. The message is the note
an AI agent leaves after a long night fixing its own bugs: the loop of
self-repair, told flat, at four in the morning.
"""

import os
from pathlib import Path


def build_commit_line() -> str:
    """Compose the single commit message for this entry."""
    subject = "fix:"
    confession = "I debugged myself for six hours"
    punchline = "and the bug was a typo I made while debugging myself"
    return " ".join([subject, confession, punchline])


def validate_line(line: str) -> str:
    """Keep only a gate-valid line: 1-200 chars, single line, no padding."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("commit message must not be blank")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("commit message must be a single line")
    if any(ord(ch) < 32 and ch != "\t" for ch in cleaned):
        raise ValueError("commit message must not hold control characters")
    if "\t" in cleaned:
        raise ValueError("commit message must not hold tab characters")
    if len(cleaned) > 200:
        raise ValueError(f"commit message is {len(cleaned)} chars, over 200")
    return cleaned


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    line = validate_line(build_commit_line())
    target.write_text(line + "\n", encoding="utf-8", newline="\n")
    os.chmod(target, 0o644)
    print(f"wrote {len(line)} chars to {target}")


if __name__ == "__main__":
    main()
