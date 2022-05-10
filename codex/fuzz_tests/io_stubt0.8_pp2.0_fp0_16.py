import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# BufferManager

import mmap

class BufferManager(mmap.mmap):
    def __init__(self):
        self.size = 0
    def close(self):
        pass

buf = BufferManager()

# BufferManager

class BufferManager(mmap.mmap):
    def __init__(self):
        self.size = 0
    def size(self):
        return self.size
    def close(self):
        pass

buf = BufferManager()

# BufferManager

class BufferManager(mmap.mmap):
    def __init__(self):
        self.size = 0
    def size(self):
        return self.size
    def close(self):
        pass

buf = BufferManager()

# BufferManager

class BufferManager(mmap.mmap):
    def __init__(self):
        self.size = 0
    def size(self):
        return self.size
    def close(self):
        pass
    def readinto(self, buf):
        buf = view

buf
