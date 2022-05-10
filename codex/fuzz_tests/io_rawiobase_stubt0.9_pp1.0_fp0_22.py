import io
class File(io.RawIOBase):
    def __init__(self,data):
        self.data=data
    def seekable(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return False
    def readinto(self,b):
        l=len(self.data)
        b[:l]=self.data
        self.data=self.data[l:] or None
        return l
f = File(b"A trivial")
isinstance(f,io.RawIOBase)

class FileObjectTranscoded(io.RawIOBase):
    import io
    def __init__(self,file,encoding):
        self._file=file
        self.encoding=encoding
        self.buffer=bytearray()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return self._file.seekable()
    def close(self):
        self._file.close()
    def seek(self,offset,whence=io.SEEK_SET
