"""Core logic to convert indents in a file from spaces to tabs"""
from __future__ import annotations

from re import sub
from typing import IO, Callable, Match

from .pass_fail_constants import FAIL, PASS


def make_substituter(chunk_size: int) -> Callable[[Match[bytes]], bytes]:
    """Create a replace function for use with Python's re.sub

    Closes-over the chunk size so the replace function may be used for
    different indentations.
    """

    def replace_spaces_with_tabs(m: Match[bytes]) -> bytes:
        """Replace spaces with tabs in a provided match

        Expects match to have two groups: the indent and the rest of the line
        """
        spaces_num = len(m[1])
        tabs = spaces_num // chunk_size * b"\t"
        spaces = spaces_num % chunk_size * b" "
        return tabs + spaces + m[2]

    return replace_spaces_with_tabs


def convert_indents(fp: IO[bytes], spaces: int) -> int:
    """Replace space indents with tabs in provided file pointer"""
    replace_spaces_with_tabs = make_substituter(spaces)

    retv = PASS
    new_contents = []

    for line in fp:
        new = sub(br"(^[ ]+)(.*$)", replace_spaces_with_tabs, line)
        new_contents.append(new)
        if new != line:
            retv = FAIL

    if retv != PASS:
        fp.seek(0)
        fp.writelines(new_contents)
        fp.truncate()

    return retv
