import io
class File(io.RawIOBase):
    def __init__(self):
        self.offset = 0
    def write(self, b):
        with open('texto.txt', 'rb+') as f:
            f.seek(self.offset)
            f.write(b)
        self.offset += len(b)
    def read(self, n=-1):
        with open('texto.txt', 'rb') as f:
            f.seek(self.offset)
            data = f.read(n)
            self.offset += len(data)
        return data
fm = File()
