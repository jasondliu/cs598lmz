import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.len = os.fstat(file.fileno()).st_size
        self.pos = 0

    def read(self, sz=-1):
        if self.pos >= self.len:
            return ''
        self.pos += sz
        return os.read(self.file.fileno(), sz)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.len + offset
        return self.pos

    def tell(self):
        return self.pos

class ZipFile(object):
    def __init__(self, file, mode='r', compression=zipfile.ZIP_STORED, allowZip64=False):
        self.file = file
        self.mode = mode
        self.compression = compression
        self.allow
