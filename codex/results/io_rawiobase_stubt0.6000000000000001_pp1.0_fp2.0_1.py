import io
class File(io.RawIOBase):
    def __init__(self, filepath, *args, **kwargs):
        self.filepath = filepath
        self.file = None
        self.args = args
        self.kwargs = kwargs
        self.open()

    def open(self):
        self.file = open(self.filepath, *self.args, **self.kwargs)

    def close(self):
        self.file.close()

    def read(self, *args, **kwargs):
        return self.file.read(*args, **kwargs)

    def readinto(self, *args, **kwargs):
        return self.file.readinto(*args, **kwargs)

class FileStream(io.RawIOBase):
    def __init__(self, filepath, *args, **kwargs):
        self.file = File(filepath, *args, **kwargs)
        self.pos = 0

    def read(self, *args, **kwargs):
        data = self.file.read(*args, **kwargs)
        self.pos +=
