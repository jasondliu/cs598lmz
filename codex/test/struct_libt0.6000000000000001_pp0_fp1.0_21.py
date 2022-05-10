import _struct
import array
import math

from . import util

def _pack(fmt, *args):
    return _struct.pack('<' + fmt, *args)

def _unpack(fmt, *args):
    return _struct.unpack('<' + fmt, *args)

class Cursor(object):
    """A memory-mapped cursor.

    This is an internal class and should not be used directly.
    """

    def __init__(self, array, address):
        self.array = array
        self.address = address

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def seek(self, address):
        self.address = address

    def seek_relative(self, offset):
        self.address += offset

    def tell(self):
        return self.address

    def read(self, size):
        data = self.array[self.address:self.address + size]
        self.address += size
        return data

