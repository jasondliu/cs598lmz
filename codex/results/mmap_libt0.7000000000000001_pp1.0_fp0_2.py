import mmap
import struct
import sys
import os

class shm_exception(Exception):
    pass

class shm_file(object):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_RDWR|os.O_CREAT, 0600)
        self.mm = mmap.mmap(self.fd, 0)
        self.header = struct.unpack('qqqq', self.mm[:32])
        self.used_size = self.header[1]
        self.total_size = self.header[2]
        self.pagesize = self.header[3]
        if self.total_size == 0:
            self.total_size = 1024 * 1024 * 32
            self.header = (0, 0, self.total_size, self.pagesize)
            self.mm.seek(0)
            self.mm.write(struct.pack('qqqq', *self.header))
            self.mm.flush()
        self.mm = mmap.mmap
