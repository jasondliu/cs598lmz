import mmap
import os
import re
import sys
import tempfile
import time

from .utils import (
    _parse_file,
    _parse_key,
    _parse_value,
    _serialize_file,
    _serialize_key,
    _serialize_value,
)

if sys.version_info[0] >= 3:
    long = int
    unicode = str


class _Mmap(mmap.mmap):
    """
    Wrapper for mmap.mmap that provides a context manager.
    """
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class _File(object):
    """
    Wrapper for file that provides a context manager.
    """
    def __init__(self, *args, **kwargs):
        self._file = open(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._file.close()

    def __get
