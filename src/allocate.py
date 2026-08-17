#! /usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "rich",
# ]
# ///

import argparse
import allocate.allocator as alloc
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description = "Per run budget allocater")
    p.add_argument(
        "total",
        help = "total amount to allocate from",
    )
    p.add_argument(
        "-f",
        "--file",
        required = True,
        help = "budgets file containing category targets",
    )
    return p.parse_args()

def main() -> int:
    args = parse_args()
    alloc.allocate_budget(int(args.total), Path(args.file))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
