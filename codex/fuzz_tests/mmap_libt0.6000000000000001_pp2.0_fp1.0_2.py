import mmap
import os
import sys

class MemoryMap(object):
    """
    A simple wrapper class for reading and writing to memory-mapped files
    """

    def __init__(self, filename):
        """
        Open a memory mapped file
        """
        self.filename = filename
        self.fd = os.open(filename, os.O_CREAT | os.O_RDWR)
        os.truncate(self.fd, 1024)
        self.map = mmap.mmap(self.fd, 1024)

    def write(self, offset, data):
        """
        Write a string of data to the memory-mapped file at the given offset
        """
        self.map.seek(offset)
        self.map.write(data)

    def read(self, offset, length):
        """
        Read a string of data from the memory-mapped file at the given offset
        and length
        """
        self.map.seek(offset)
        return self.map.read(length)

    def close(self):
        """
        Close the memory
