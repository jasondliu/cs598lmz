import io
class File(io.RawIOBase):
    """
    A raw file-like object.
    """
File.__doc__ = io.RawIOBase.__doc__
File.__module__ = __name__

import os
import math
import mmap
try:
    import fcntl
except ImportError:
    have_fcntl = False
else:
    have_fcntl = True

def open(filename, mode="rb", buffering=-1, **kwargs):
    if "b" not in mode:
        mode += "b"
    return io.open(filename, mode, buffering, **kwargs)

class MapFile(File):
    """
    A file-like object backed by a memory-mapped file.
    """
    def __init__(self, *args, **kwargs):
        File.__init__(self, *args, **kwargs)
        self.map = None
        self.mmap = mmap.mmap(-1, 0, access=mmap.ACCESS_READ)

    def fileno(self):
        return self.mmap.
