import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
        self.mode = mode
        self.closed = False
        self.softspace = 0

    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        self.closed = True
        self.file.close()

    def __del__(self):
        try:
            self.close()
        except:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def readinto(self, b):
       
