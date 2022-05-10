import mmap
import struct
import sys
import time

from enum import Enum

# ------------------------------------------------------------------------------

class MemoryMap:
    def __init__(self, mmap_file, size):
        self.mmap_file = mmap_file
        self.size = size
        self.mmap = mmap.mmap(mmap_file.fileno(), size)
        self.last_update = 0

    def read(self, offset, length):
        return self.mmap[offset:offset+length]

    def write(self, offset, data):
        self.mmap[offset:offset+len(data)] = data
        self.mmap.flush()
        self.mmap.seek(offset)

    def read_int(self, offset):
        return struct.unpack('i', self.read(offset, 4))[0]

    def write_int(self, offset, value):
        self.write(offset, struct.pack('i', value))

