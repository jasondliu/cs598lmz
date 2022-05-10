import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.f = open(path, "rb")


    def seekable(self):
        return True


    def readable(self):
        return True


    def writable(self):
        return False


    def tell(self):
        return self.f.tell()


    def seek(self, offset, whence=io.SEEK_SET):
        self.f.seek(offset, whence)


    def readline(self):
        return self.f.readline()


    def read(self, size=-1):
        return self.f.read(size)


    def write(self, data):
        raise NotImplementedError()


    def flush(self):
        self.f.flush()


    def close(self):
        self.f.close()


    def peek(self, size=1):
        offset = self.f.tell()
        try:
            return self.f.read(size)
        finally:
            self.f.seek(offset)



