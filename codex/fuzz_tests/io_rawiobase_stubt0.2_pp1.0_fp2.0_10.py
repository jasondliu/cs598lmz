import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

def get_file_handle(file_name, mode='r'):
    if isinstance(file_name, str):
        return open(file_name, mode)
    elif isinstance(file_name, io.IOBase):
        return file_name
    elif isinstance(file_name, File):
        return file_name.file
    else:
        raise TypeError('file_name must be a string or a file handle')

def get_file_name(file_name):
    if isinstance(file_name,
