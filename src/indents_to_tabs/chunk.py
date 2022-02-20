"""Chunk data into sequences of data of a specific size/length."""
from __future__ import annotations

from typing import Generator


def chunk(chunk_size: int, b: bytes) -> Generator[bytes, None, None]:
    """Yield chunks of bytes in specific size.

    >>> list(chunk(2, b'abcdefghi'))
    [b'ab', b'cd', b'ef', b'gh', b'i']
    >>> list(chunk(4, b'abcdefghi'))
    [b'abcd', b'efgh', b'i']
    """
    for i in range(0, len(b), chunk_size):
        yield b[i : i + chunk_size]
