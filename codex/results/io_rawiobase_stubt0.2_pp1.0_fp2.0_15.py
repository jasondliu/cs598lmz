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
    def write(self, b):
        return self.file.write(b)
    def writable(self):
        return True
    def close(self):
        self.file.close()

def _get_file_handle(file):
    if isinstance(file, io.RawIOBase):
        return file
    elif hasattr(file, 'read') or hasattr(file, 'write'):
        return File(file)
    else:
        raise TypeError("Invalid file object: %r" % (file,))

def _get_file_handle_and_close(file):
    if isinstance(file,
