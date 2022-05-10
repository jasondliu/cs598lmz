import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-1):
        self.file.seek(self.offset)
        s = self.file.read(n)
        self.offset += len(s)
        return s
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            self.offset = self.file.size + offset
        else:
            raise ValueError("Invalid value for whence")
    def tell(self):
        return self.offset
    def readable(self):
        return True
    def writable(self):
        return False
    def flush(self):
        pass
    def close(self):
        pass

def get_file_size(file):
    file.
