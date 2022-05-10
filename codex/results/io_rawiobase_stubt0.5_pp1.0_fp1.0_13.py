import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    def close(self):
        pass
    def write(self, b):
        print(b)
    def read(self, size=-1):
        return b"\x00" * size
    def fileno(self):
        return 0
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def readable(self):
        return "r" in self.mode
    def writable(self):
        return "w" in self.mode

f = File("test.txt", "w+")
f.write(b"Hello, World")
f.seek(0)
f.read()
f.close()
</code>

