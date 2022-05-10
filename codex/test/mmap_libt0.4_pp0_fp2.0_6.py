import mmap
import struct
import os

class MMap:
    def __init__(self, file_name, size, offset=0):
        self.file_name = file_name
        self.size = size
        self.offset = offset
        self.fd = os.open(file_name, os.O_RDWR)
        self.mm = mmap.mmap(self.fd, self.size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=self.offset)

    def __del__(self):
        self.mm.close()
        os.close(self.fd)

    def read(self, addr, size):
        return self.mm[addr:addr+size]

    def write(self, addr, data):
        self.mm[addr:addr+len(data)] = data

    def read_u32(self, addr):
        return struct.unpack('I', self.read(addr, 4))[0]

