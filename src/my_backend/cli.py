"""Command-line example for the starter package."""

import argparse

from .process import total_count


def main() -> int:
    parser = argparse.ArgumentParser(description="Add example counts.")
    parser.add_argument("counts", nargs="+", type=int, help="Integer counts to sum.")
    args = parser.parse_args()
    print(total_count(args.counts))
    return 0
