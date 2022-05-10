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
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.seek(0, io.SEEK_END)
        self.offset = offset
    def tell(self):
        return self.offset

def get_file(file):
    return File(file)

def get_file_size(file):
    return file.seek(0, io.SEEK_END)

def get_file_offset(file):
    return file.tell()

def set_file_offset(file, offset):
    file.seek(offset)

def read_file(file, size
