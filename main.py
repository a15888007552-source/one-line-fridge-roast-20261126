"""Write the smart-fridge roast to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from pathlib import Path
import os

LINE = "My smart fridge has Wi-Fi, a camera and a touchscreen, but it can't explain the lone pickle at the back that expired during the Obama administration."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
