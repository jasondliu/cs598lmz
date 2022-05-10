import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')


class SharedMemory(object):
    """
    Shared memory object using ctypes and the system's mmap functions.
    """
    def __init__(self, size=4096, tagname=None, dtype='d', readonly=False,
                 verbose=False):
        """
        Initialize a new SharedMemory object.

        Parameters
        ----------
        size : int, optional
            Size of the shared memory block in bytes. Default is 4096.
        tagname : str, optional
            Name of the shared memory block. Default is None, which means a
            random tag is generated.
        dtype : str, optional
            Data type of the shared memory block. Default is 'd' (i.e. double).
        readonly : bool, optional
            Whether the shared memory block should be read-only.
        verbose : bool, optional
            Whether to print debug messages.
        """
        self.size = size
        self.tagname = tagname
        self.dtype = dtype
        self.readonly = readonly
       
