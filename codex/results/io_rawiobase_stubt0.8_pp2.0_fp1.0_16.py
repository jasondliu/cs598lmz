import io
class File(io.RawIOBase):

    def __init__(self, fname, mode='r'):
        self.file = open(fname, mode)
        self.pos = 0

    def readable(self):
        return True

    def readinto(self, b):
        data = self.file.read(len(b))
        b[:] = data
        self.pos += len(data)
        return len(data)

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.pos
        elif whence == io.SEEK_END:
            offset += self.file.tell()
        self.pos = self.file.seek(offset)
        return self.pos

class Archive(File):
    # UNZ_MAXFILENAMEINZIP = 256
    # UNZ_MAXCOMMENT = 256
    # UNZ_OK = 0
    # UNZ_END_OF_LIST_OF_FILE = -100
    # UNZ_T
