import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b) # b will be written to from offset 0
        view = memoryview(b).cast('B')
        while n > 0:
            buf = self.file.read(n)
            if not buf:
                break
            view[:len(buf)] = buf
            view = view[len(buf):]
            n -= len(buf)
        return len(b) - n
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def tell(self):
        return self.file.tell()
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

class ZipExtFile(io.
