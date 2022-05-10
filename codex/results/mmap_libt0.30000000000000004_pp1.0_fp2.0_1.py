import mmap
import re
import sys
import time
import traceback

from . import _util


class _LogFile(object):
    """A file-like object that reads from a file and keeps track of the current
    position.

    This is used to read from the log file and keep track of the current
    position.
    """

    def __init__(self, file_path):
        self._file_path = file_path
        self._file = None
        self._pos = 0

    def __enter__(self):
        self._file = open(self._file_path, 'r')
        self._file.seek(0, os.SEEK_END)
        self._pos = self._file.tell()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()

    def read(self, size=None):
        """Reads up to the specified number of bytes.

        If size is not specified, reads until the end of the file.
        """
        self._file.seek(self._pos
