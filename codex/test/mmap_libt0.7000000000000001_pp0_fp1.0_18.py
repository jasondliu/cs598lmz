import mmap
import shutil
import struct
import sys

__author__ = 'Nicklas Boerjesson'


class BinaryReader(object):
    """
    Provide a binary file reader for Python. The reader is based on a file
    object and can be used in a with-statement or as a context manager.

    Usage:
    with BinaryReader(file_object) as _reader:
        _reader.read_int()
    """

    def __init__(self, _file, _read_buffer_size=None):
        """
        Initialize the reader by providing a file object.
        :param _file: A file object.
        :param _read_buffer_size: The size of the buffer to use when reading.
        """
        if _read_buffer_size is None:
            self.read_buffer_size = 8192
        else:
            self.read_buffer_size = _read_buffer_size

        self.file = _file
        self.mm = mmap.mmap(_file.fileno(), 0, access=mmap.ACCESS_READ)
        self
