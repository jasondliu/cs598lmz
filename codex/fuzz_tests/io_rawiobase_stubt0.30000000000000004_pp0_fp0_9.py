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
    def close(self):
        self.file.close()

def get_file_object(file, mode='r'):
    if isinstance(file, str):
        return open(file, mode)
    elif isinstance(file, io.IOBase):
        return file
    else:
        return File(file)

def get_file_name(file):
    if isinstance(file, str):
        return file
    elif isinstance(file, io.IOBase):
        return file.name
    else:
        return None

def get_file_extension(file):
    name = get_file_
