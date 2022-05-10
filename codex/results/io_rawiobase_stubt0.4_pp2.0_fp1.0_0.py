import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self, n=-1):
        return self.f.read(n)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

f = File(open('/etc/passwd', 'rb'))
print(f.read(16))
print(f.tell())
f.seek(10)
print(f.tell())
print(f.read(1))
print(f.read(5))
print(f.seekable())

import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self, n=-1):
        return self.f.read(n)

    def readable(self):
        return True

    def seekable(self):
