import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

class FileWrapper(object):
    def __init__(self, file):
        self.file = file
    def __getattr__(self, name):
        return getattr(self.file, name)

def wrap_file(file, buffer_size=8192):
    """Wrap a filelike object with an adapter to make it work as a stream."""
    if isinstance(file, io.IOBase):
        return file
    else:
        return FileWrapper(File(file))

def make_chunks(file, chunk_size=8
