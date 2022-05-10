import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            r = self.file.readinto(view)
            view = view[r:]
            n -= r
            if r == 0:
                break
        return len(b) - n
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        return self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def open(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd
