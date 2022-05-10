import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.start = f.tell()
    def tell(self):
        return self.f.tell() - self.start
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            offset += self.start
        self.f.seek(offset, whence)
    def readinto(self, b):
        return self.f.readinto(b)
    def read(self, n=-1):
        return self.f.read(n)
    def close(self):
        return self.f.close()

def read_file(f, offset=0, size=None):
    f.seek(offset)
    if size is None:
        size = os.fstat(f.fileno()).st_size - offset
    return File(f)

def read_file_from_archive(archive, path, offset=0, size=None):
    f = archive.open(path, mode='rb')
    return
