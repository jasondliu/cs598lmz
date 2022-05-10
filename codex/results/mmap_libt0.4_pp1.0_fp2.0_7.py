import mmap
import os

from collections import defaultdict

from . import _util
from ._util import _decode_path
from . import _compat as _c

_c.check_version("3.3", "mmap.ACCESS_WRITE")

_fmt_size = struct.calcsize("!I")


class _MmapFile(object):
    def __init__(self, file, access=mmap.ACCESS_WRITE):
        self._file = file
        self._mmap = mmap.mmap(
            file.fileno(),
            0,
            access=access,
            prot=mmap.PROT_READ | mmap.PROT_WRITE,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._mmap.close()
        self._file.close()
        self._file = None
        self._mmap = None

    def read(
