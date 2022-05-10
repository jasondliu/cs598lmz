import ctypes
import ctypes.util
import threading
import sqlite3

class _MemMap(object):
    """
    A memory mapped file object.  This is used by _DictMemMap and may be used
    directly for other purposes.
    """
    def __init__(self, filename, size, start = 0):
        self.filename = filename
        self.size = size
        self.start = start

        self.file = os.open(filename, os.O_RDWR)
        self._map_handle = mmap.mmap(self.file, size, mmap.MAP_SHARED,
                                     mmap.PROT_READ | mmap.PROT_WRITE,
                                     offset = start)

    def length(self):
        return self.size

    def get_as(self, dtype):
        """
        Takes a dtype and returns a numpy array that is a view of the file
        """
        return np.frombuffer(self._map_handle, dtype = dtype)

    def get_as_str(self, offset = 0):
        return self._map_handle[offset:].trans
