import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'rb')
    def read(self, n):
        return self.f.read(n)
    def seek(self, n):
        return self.f.seek(n)
    def close(self):
        return self.f.close()
    def tell(self):
        return self.f.tell()
    def __del__(self):
        self.close()

class File_with_name(File):
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'rb')
    def name(self):
        return self.path

class File_with_size(File):
    def __init__(self, path):
        self.path = path
        self.f = open(path, 'rb')
    def size(self):
        return os.stat(self.path).st_size

class File_with_name_and_size(File_with_name, File
