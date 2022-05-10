import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def close(self):
        self.file.close()

class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    def __getattr__(self, name):
        return getattr(self.file, name)

def wrap_file(file):
    if isinstance(file, io.RawIOBase):
        return file
    return FileWrapper(file)

def wrap_file_in_stream(file):
    if isinstance(file, io.RawIOBase):
        return file
    return File(file)

def wrap_file_in_stream_with_close(file):
    if isinstance(file, io.RawIOBase
