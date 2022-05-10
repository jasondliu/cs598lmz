import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def seekable(self):
        return True
    def readable(self):
        return True
    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = len(b)
        chunk = self.file.read(self.offset, l)
        b[:len(chunk)] = chunk
        self.offset += len(chunk)
        return len(chunk)
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size()
        self.offset = offset
        return self.offset
    def tell(self):
        return self.offset
    def close(self):
        pass

class FileSystem(object):
    def __init__(self, storage):
        self.storage =
