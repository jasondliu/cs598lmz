import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util
from . import xdg

# -----------------------------------------------------------------------------

_log = log.get_logger(__name__)

# -----------------------------------------------------------------------------

class _File(object):
    """
    A file object that can be used to read and write to a file.
    """

    def __init__(self, path, mode='r'):
        self._path = path
        self._mode = mode
        self._file = None
        self._mmap = None
        self._size = None
        self._pos = 0

    def __enter__(self):
        self._file = open(self._path, self._mode)
        self._size = os.fstat(self._file.fileno()).st_size
        if self._mode == 'r':
            self._mmap = mmap.mmap(self._file.fileno(), self._size,
                                   access=mmap.ACCESS_READ
