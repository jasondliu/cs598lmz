import mmap
import struct

class MmapFile:
    def __init__(self, filename):
        self.filename = filename
        self.infile = open(self.filename, "rb")
        self.mmapfile = mmap.mmap(self.infile.fileno(), 0, access=mmap.ACCESS_READ)
        self.max_pos = len(self.mmapfile)
        self.pos = 0

    def read(self, size):
        if self.pos + size > self.max_pos:
            raise IOError("Read beyond end of file")
        res = self.mmapfile[self.pos:self.pos+size]
        self.pos += size
        return res

    def close(self):
        self.mmapfile.close()
        self.infile.close()

class MmapFileWriter:
    def __init__(self, filename, size):
        self.filename = filename
        self.outfile = open(self.filename, "wb")
        self.outfile.write("\x00"*size)

