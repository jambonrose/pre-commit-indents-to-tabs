"""Replace spaces with tabs in lines that begin with spaces."""
from __future__ import annotations

import argparse
from typing import Sequence

from .convert import convert_indents

__version__ = "0.0.1"


def main(argv: Sequence[str] | None = None) -> int:
    """Convert indents when invoked from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="+",
        type=argparse.FileType("rb+"),
        help="Files to convert",
    )
    parser.add_argument(
        "--spaces",
        type=int,
        default=2,
        metavar="INTEGER",
        help="How many spaces to replace with a tab",
    )
    args = parser.parse_args(argv)

    return convert_indents(args.filenames, args.spaces)


if __name__ == "__main__":
    raise SystemExit(main())
