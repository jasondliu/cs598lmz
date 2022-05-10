import io
# Test io.RawIOBase
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = io.open(filename, 'rb')
        self.file = open(filename, 'rb')
        width, height, self.pixels = [int(x) for x in self.file.readline().split()]
        self.x, self.y = 0, 0

    def read(self, n=0):
        if not n:
            n = len(self.pixels) - self.x
        data = self.pixels[self.x:self.x+n]
        if len(data) != n:
            self.x = len(self.pixels)
            raise EOFError('Cannot read requested number of bytes')
        self.x += n
        return data

    def seek(self, n, whence=0):
        if whence == 0:
            self.x = n
        elif whence == 1:
            self.x = min(len(self.pixels), self.x + n)
        elif whence == 2:
