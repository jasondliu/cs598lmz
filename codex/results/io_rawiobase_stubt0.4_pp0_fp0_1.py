import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

def get_file_size(file):
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size

def get_file_name(file):
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size

def get_file_name(file):
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size

def get_file_name(file):
    file.seek(0, 2)
    size = file.tell()
