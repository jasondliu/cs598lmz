import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        self.file = open(self.filename, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def __iter__(self):
        return self
    def __next__(self):
        b = bytearray(1)
        l = self.readinto(b)
        if l == 0:
            raise StopIteration
        return b[0]
    def next(self):
        return self.__next__()

# Test the file
with File('test.txt') as f:
    for byte in f:
        print(byte)
</code>

