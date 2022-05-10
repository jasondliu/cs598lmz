import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.read(n)
            view[:len(r)] = r
            view = view[len(r):]
            n -= len(r)
        return len(b)
    def write(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.write(view)
            view = view[r:]
            n -= r
        return len(b)
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()
    def seekable(self):
        return self.file.seekable()
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell
