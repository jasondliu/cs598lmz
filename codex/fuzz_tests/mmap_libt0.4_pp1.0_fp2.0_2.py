import mmap
import re
import os

from . import _util


class MMapFile(object):
    """
    A memory-mapped file.

    This class is a wrapper around the Python mmap module. It provides a
    simple interface to memory-mapped files.

    :param filename: The name of the file to open.
    :param mode: The mode to open the file in.
    :param offset: The offset in the file to start mapping at.
    :param length: The number of bytes to map.
    :param access: The access flags for the file.
    """

    def __init__(self, filename, mode='r', offset=0, length=None, access=mmap.ACCESS_WRITE):
        self.filename = filename
        self.mode = mode
        self.offset = offset
        self.length = length
        self.access = access

        self._open_file()
        self._map_file()

    def __getitem__(self, key):
        return self.mmap[key]

    def __setitem__(self, key, value
