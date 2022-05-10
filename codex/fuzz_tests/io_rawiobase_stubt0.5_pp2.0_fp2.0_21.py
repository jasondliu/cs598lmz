import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
        self.closed = False
    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        self.closed = True
    def readable(self):
        return True
    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = len(b)
        chunk = self.file.read(self.offset, l)
        b[:len(chunk)] = chunk
        self.offset += len(chunk)
        return len(chunk)

class Chunk(object):
    def __init__(self, file, offset, length):
        self.file = file
        self.offset = offset
        self.length = length
    def read(self, offset, length):
        return self.file.read(self.offset+offset, length)

class FileSystem(object):
    def __init__(self, fs):

