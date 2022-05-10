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

class FileWriter(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
    def write(self, data):
        buf[len(buf):] = data
    def writable(self):
        return True

buf = bytearray()
f = io.BufferedWriter(FileWriter(buf))
f.write(b"abc")
del f

class FileReader(io.IOBase):
    def __init__(self, buf):
        self.buf = buf
        self.ptr = 0
    def read(self, n = -1):
        if n == 0:
            return b""
        if n < 0 or n > len(self.buf) - self.ptr:
            n = len(self.buf) - self.ptr
        data = self.buf[self.ptr:self.ptr+n]
        self.ptr += n
        return data
    def readable(self):
        return True

buf = bytearray(b"abcdef")
f = io.TextIOWrapper
