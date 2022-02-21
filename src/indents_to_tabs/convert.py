"""Core logic to convert indents in a file from spaces to tabs"""
from __future__ import annotations

from re import compile as re_compile, sub
from typing import IO, Callable, Match, Pattern, Sequence, TypeVar

from .pass_fail_constants import FAIL, PASS


def make_indent_replacer(
    chunk_size: int,
) -> tuple[Pattern[bytes], Callable[[Match[bytes]], bytes]]:
    """Create pattern & replace function for use with Python's re.sub

    Closes-over the chunk size so the replace function may be used for
    different indentations.
    """
    pattern = re_compile(br"(^[ ]+)(.*$)")

    def replace_spaces_with_tabs(m: Match[bytes]) -> bytes:
        """Replace spaces with tabs in a provided match

        Expects match to have two groups: the indent and the rest of the line
        """
        spaces_num = len(m[1])
        tabs = spaces_num // chunk_size * b"\t"
        spaces = spaces_num % chunk_size * b" "
        return tabs + spaces + m[2]

    return pattern, replace_spaces_with_tabs


S = TypeVar("S", str, bytes)  # Must be str or bytes


def replace_in_file(
    fp: IO[S], pattern: S | Pattern[S], replace: Callable[[Match[S]], S]
) -> int:
    """Use re.sub to replace all lines in fp matching pattern.

    Write new contents to file.

    Return PASS (int 0) if file is unchanged, or FAIL (int 1) if file
    is changed.

    If the file is in standard modes (e.g.: 'r'), then the pattern must
    be a string and the replace function must handle strings. However,
    if the file is in bytes mode (e.g.: 'rb', 'wb', etc), the pattern
    provided must be in bytes, and the replace function must handle
    bytes.
    """
    retv = PASS
    new_contents = []

    for line in fp:
        new = sub(pattern, replace, line)
        new_contents.append(new)
        if new != line:
            retv = FAIL

    if retv != PASS:
        fp.seek(0)
        fp.writelines(new_contents)
        fp.truncate()

    return retv


def convert_indents(files: Sequence[IO[bytes]], spaces: int) -> int:
    """Convert n spaces to tabs in indents of each file provided"""
    pattern, replace_spaces_with_tabs = make_indent_replacer(spaces)

    retv = PASS
    for fp in files:
        file_retv = replace_in_file(fp, pattern, replace_spaces_with_tabs)
        retv |= file_retv

    return retv
