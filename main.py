#!/usr/bin/env python3
"""One Line, No Deadline Met (make.fun bounty
u-markk-st-one-line-no-deadline-met-6adc00ce).

Writes one line to /output/entry.txt: a one-line joke that gives an
excuse for missing a deadline.

The line, built against the judge's brief in the kit's RULES.txt,
in the brief's own order:
  1. Excuse for a missed deadline: the speaker did submit on time --
     to the wrong chat -- so the deadline was missed by misdelivery,
     not by doing nothing.
  2. Funny, with a turn: the setup sounds like a plain apology for
     being late, then flips -- the work exists, it just went to the
     wrong audience.
  3. One-line form: a single sentence that reads cleanly aloud; the
     punch ("thinks I'm a genius") lands on the last words.
  4. Sounds like a person cornered: a sheepish, slightly proud
     confession, exaggerated just enough -- the wrong chat now
     admires work it never asked for.
  5. Fresh: no dog, no alarm clock, no traffic, no Wi-Fi died -- the
     excuse is misdelivery to an audience that likes it.

Rejected alternatives: Wi-Fi died mid-upload, then an hour explaining
to the router that it had one job (funny personification, but "my
internet died" is a heard-before excuse family); the file was ready
at 8:59 when the laptop restarted for updates (concrete, but the
forced-update trope is stock); the deadline moved to another timezone
without telling me (short and punchy, but the turn is thin and the
excuse is a shrug, not a joke). The wrong-chat line wins on the
judge's own order: its surprise is last, its landing is the most
sudden, and its angle is the freshest.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = "I submitted it right on time \u2014 to the wrong chat, where my group project now thinks I'm a genius."


def _validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 chars, one line,
    not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if text != text.strip():
        raise ValueError("joke must not start or end with whitespace")
    if not text.endswith("."):
        raise ValueError("joke must be one sentence ending with a full stop")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("joke must not contain control characters")


def write_entry(text: str, out_dir: str) -> str:
    """Validate the entry, then write it to <out_dir>/entry.txt.

    Returns the path written. The file holds exactly the validated
    text -- no trailing newline, no extra bytes.
    """
    _validate(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(JOKE, out_dir)


if __name__ == "__main__":
    main()
