import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def read(self, n= -1):
        return n
    def write(self, n= -1):
        return n
    def close(self):
        pass
    def seek(self, n, whence=0):
        if __verbose__:
            print("seek called with " + "whence: " + str(whence) + " n: " + str(n))
        return 0
    def tell(self):
        return 0
    def fileno(self):
        return 0
    def isatty(self):
        return False
    def flush(self):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __next__(self):
        return ''
    def __iter__(self):
        return self
    def truncate(self, n=0):
        return 0

for m in ['file', 'FileIO', 'BlockingIOError', 'UnsupportedOperation',
