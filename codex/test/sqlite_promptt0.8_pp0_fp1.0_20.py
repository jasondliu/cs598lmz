import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Set the image database path
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
libc.malloc.argtypes = [ctypes.c_size_t]
libc.malloc.restype = ctypes.c_void_p

def malloc(size):
    addr = libc.malloc(size)
    if not addr:
        raise MemoryError()
    return ctypes.c_void_p(addr)

class ImageCluster(object):
    def __init__(self, process_name='', image_base=0, image_size=0, image_path='', image_name='', image_ext=''):
        self.process_name = process_name
        self.image_base = image_base
        self.image_size = image_size
        self.image_path = image_path
        self.image_name = image_name
        self.image_ext = image_ext

