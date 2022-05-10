import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast("B")
        while n > 0:
            r = self.file.read(n)
            view[:len(r)] = r
            view = view[len(r):]
            n -= len(r)
        return len(b)

def test():
    f = open("test.txt", "rb")
    f = File(f)
    print(f.read(5))
    print(f.read(5))
    print(f.read(5))
    print(f.read(5))
