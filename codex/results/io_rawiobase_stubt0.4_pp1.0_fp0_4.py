import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.size = os.path.getsize(path)

    def read(self, size=-1):
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        return self.file.close()

class FileSystem(object):
    def __init__(self):
        self.files = {}

    def add(self, path):
        self.files[path] = File(path)

    def get(self, path):
        return self.files[path]

class FileSystemHandler(object):
    def __init__(self, filesystem):
        self.filesystem = filesystem

    def __getattr__(self, path):
        return self.filesystem.get(path)

class FileHandler(object):

