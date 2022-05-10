import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.f = open(path, mode)

    def read(self, size=-1):
        return self.f.read(size)

    def write(self, b):
        return self.f.write(b)

    def fileno(self):
        return self.f.fileno()

    def close(self):
        return self.f.close()

class FileObject(io.IOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.f = open(path, mode)

    def read(self, size=-1):
        return self.f.read(size)

    def write(self, b):
        return self.f.write(b)

    def fileno(self):
        return self.f.fileno()

    def close(self):
        return self.f.close()

class FileDescriptor(io.RawIOBase):

