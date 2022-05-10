import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.file = open(filepath, 'rb')

    def read(self, size=-1):
        return self.file.read(size)

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

    def close(self):
        self.file.close()

class FileSystem(object):
    def __init__(self, path):
        self.path = path

    def open(self, filepath, mode='r'):
        return open(os.path.join(self.path, filepath), mode)

    def listdir(self, path):
        return os.listdir(os.path.join(self.path, path))

    def isdir(self, path):
        return os.path.isdir(os
