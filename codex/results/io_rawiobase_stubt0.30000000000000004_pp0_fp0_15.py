import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.offset = offset
        elif whence == io.SEEK_CUR:
            self.offset += offset
        elif whence == io.SEEK_END:
            raise NotImplementedError("Cannot use SEEK_END")
        else:
            raise ValueError("Invalid whence (%r, should be %d, %d, %d)" % (whence, io.SEEK_SET, io.SEEK_CUR, io.SEEK_END))
        self.file.seek(self.offset)

    def tell(self):
        return self.offset

class FileReader(File):
    def __init__(self, file):
        super().__init__(file)
       
