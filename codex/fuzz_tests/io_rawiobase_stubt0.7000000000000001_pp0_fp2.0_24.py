import io
class File(io.RawIOBase):
    def __init__(self):
        self.pos = 0
    def read(self, size):
        self.pos += size
        return b"\0" * size
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        else:
            self.pos = len(self) + offset
        return self.pos
    def tell(self):
        return self.pos
    def write(self, data):
        raise NotImplementedError
    def writable(self):
        return False
    def writelines(self, lines):
        raise NotImplementedError

f = File()
print(f.seekable())
print(f.readable())
print(f.tell())
print(f.seek(3, 1))
print(f.seek(2))
print(f.read(5))
print(f.tell())
print(
