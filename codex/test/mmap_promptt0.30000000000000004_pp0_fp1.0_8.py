import mmap
# Test mmap.mmap

class MMap:
    def __init__(self, filename, size):
        self.filename = filename
        self.size = size
        self.fd = os.open(filename, os.O_RDWR | os.O_CREAT)
        self.m = mmap.mmap(self.fd, size)
        self.m.seek(0)
        self.m.write(b'\x00' * size)

    def __del__(self):
        self.m.close()
        os.close(self.fd)

    def write(self, offset, data):
        self.m.seek(offset)
        self.m.write(data)

    def read(self, offset, size):
        self.m.seek(offset)
        return self.m.read(size)

    def __getitem__(self, offset):
        return self.read(offset, 1)

    def __setitem__(self, offset, data):
        self.write(offset, data)

m = MMap('test.mmap', 1024)
