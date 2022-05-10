import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.offset = 0
    def read(self, size=-1):
        self.f.seek(self.offset)
        data = self.f.read(size)
        self.offset += len(data)
        return data
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.f.seek(0, 2) + offset
        return self.offset
    def tell(self):
        return self.offset
    def fileno(self):
        return self.f.fileno()

def test_file():
    with open("sample.txt", "rb") as f:
        file = File(f)
        print(file.tell())
        print(file.read())
        print(file.read())
        print(file.seek(10))
        print(file.read())

class Monitor(
