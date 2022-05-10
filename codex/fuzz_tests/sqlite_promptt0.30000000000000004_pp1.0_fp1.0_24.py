import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

def get_shared_memory_id(name):
    """
    Get the shared memory id for a given name.
    """
    shm_open = ctypes.CDLL(ctypes.util.find_library('c')).shm_open
    shm_open.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
    shm_open.restype = ctypes.c_int
    shm_unlink = ctypes.CDLL(ctypes.util.find_library('c')).shm_unlink
    shm_unlink.argtypes = [ctypes.c_char_p]
    shm_unlink.restype = ctypes.c_int
    try:
        return shm_open('/' + name, os.O_RDWR | os.O_CREAT, 0o600)
    except:
        shm_unlink('/' + name)
        return shm_open('/' + name, os
