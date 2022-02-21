"""Utility functions to make using test data easier."""
from io import BytesIO
from pathlib import Path
from typing import IO


def _build_path(file_name: str) -> Path:
    """Build path to test data file based on file name."""
    test_dir = Path(__file__).parent
    return test_dir / "testdata" / file_name


def load_file(file_name: str) -> bytes:
    """Load contents of file as bytes"""
    with open(_build_path(file_name), "rb") as fp:
        return fp.read()


def load_file_to_buffer(file_name: str) -> IO[bytes]:
    """Load contents of file as buffer of bytes"""
    with open(_build_path(file_name), "rb") as fp:
        return BytesIO(fp.read())
