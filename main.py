import os
from pathlib import Path

JOKE = "My coding agent fixed our race condition by spawning three subagents. They all merged at once; the merge conflict got promoted to project manager."
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
