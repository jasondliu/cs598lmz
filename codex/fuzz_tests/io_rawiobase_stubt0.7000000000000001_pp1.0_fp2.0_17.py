import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def seek(self, offset, whence=None):
        if whence == None:
            self.offset = offset
        else:
            if whence == os.SEEK_SET:
                self.offset = offset
            elif whence == os.SEEK_CUR:
                self.offset += offset
            elif whence == os.SEEK_END:
                self.offset = len(self.file) + offset
        return self.offset
    def read(self, n=-1):
        if n >= 0:
            result = self.file[self.offset:self.offset+n]
            self.offset += len(result)
            return result
        else:
            result = self.file[self.offset:]
            self.offset = len(self.file)
            return result
    def tell(self):
        return self.offset
    def close(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self,
