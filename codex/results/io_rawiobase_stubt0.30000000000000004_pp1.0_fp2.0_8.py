import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def open(self):
        if self.file is None:
            self.file = open(self.filename, self.mode)
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return self.mode.startswith('r')
    def writable(self):
        return self.mode.startswith('w')
    def readinto(self, b):
        self.open()
        return self.file.readinto(b)
    def write(self, b):
        self.open()
        return self.file.write(b)
    def __del__(self):
        self.close()

f = File('file.txt', 'w')
f.write(b'hello')
f.close()
f = File('file.txt', 'r')
print(f.read())
f
