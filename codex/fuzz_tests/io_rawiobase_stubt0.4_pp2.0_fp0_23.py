import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.f = io.open(filename, 'rb')

    def read(self, size=-1):
        return self.f.read(size)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def close(self):
        return self.f.close()

class FileHandle(object):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

class FileManager(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = File(self.filename)
        return File
