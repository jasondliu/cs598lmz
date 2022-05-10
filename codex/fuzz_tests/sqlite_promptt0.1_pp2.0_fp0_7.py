import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

class SharedMemory(object):
    """
    Shared memory object.
    """
    def __init__(self, size, name=None, create=False):
        """
        Create a shared memory object.
        """
        self.size = size
        self.name = name
        self.create = create
        self.shm = None
        self.lock = threading.Lock()

    def __enter__(self):
        """
        Open the shared memory object.
        """
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the shared memory object.
        """
        self.close()

    def open(self):
        """
        Open the shared memory object.
        """
        if self.shm is not None:
            raise RuntimeError('Shared memory object is already open')
        if self.name is None:
            raise RuntimeError('Shared memory object name is not set')
        if self
