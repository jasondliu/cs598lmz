import mmap
import os

class MemMap:
    def __init__(self, filename):
        self.filename = filename

        if not os.path.isfile(self.filename):
            raise IOError(self.filename + " is not a file")

    def read(self):
        with open(self.filename, 'rb') as f:
            m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            return m.read()

    def write(self, content):
        with open(self.filename, 'wb') as f:
            m = mmap.mmap(f.fileno(), 0)
            m.write(content)

    def append(self, content):
        with open(self.filename, 'ab') as f:
            m = mmap.mmap(f.fileno(), 0)
            m.write(content)

    def prepend(self, content):
        with open(self.filename, 'r+b') as f:
            m = mmap.mmap(f.fileno(), 0
