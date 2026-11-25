"""Dad Joke Showdown entry.

Writes one dad joke to entry.txt inside the output directory.
The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable and falls back to /output, matching the make.fun runner.
"""

import os

JOKE = "I used to hate beards, but then it grew on me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
