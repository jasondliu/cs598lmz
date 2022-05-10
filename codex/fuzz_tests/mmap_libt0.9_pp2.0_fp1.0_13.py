import mmap
import string
import os.path


class MMapIterator:
    def __init__(self, mm):
        self.mm = mm
        self.const_buf = mm.read(mm.size())
        self.cur_pos = 0

    def next(self):
        if len(self.const_buf) < self.cur_pos + 1:
            raise StopIteration()
        byte = ord(self.const_buf[self.cur_pos])
        self.cur_pos += 1
        return byte


class MMap:
    def __init__(self, size):
        self.fd = os.open('/dev/zero', os.O_RDWR)
        self.mm = mmap.mmap(self.fd, size, flags=mmap.MAP_SHARED, prot=mmap.PROT_READ | mmap.PROT_WRITE)

    def write(self, bytes, offset):
        self.mm[offset: offset + len(bytes)] = bytes

    def size(self):
        return self.mm.size()

   
