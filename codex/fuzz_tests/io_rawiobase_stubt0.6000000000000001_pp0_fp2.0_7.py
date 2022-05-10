import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        self.file.write(b)
    def close(self):
        self.file.close()

class File2(File):
    pass

f = open("test.txt", "wb")
f.write(b"hello world")
f.close()

f = open("test.txt", "rb")

#f2 = File(f)
f2 = File2(f)

print(f2.read(4))
f2.seek(6)
print(f2.read())
f2.close()
