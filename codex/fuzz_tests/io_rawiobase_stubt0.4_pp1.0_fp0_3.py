import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(*args, **kwargs)
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

class FileWrapper(object):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(*args, **kwargs)
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        return self.file.write(b)
    def close(self):
        return self.file.close()

class FileWrapper2(object):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super().__init__(*args, **kwargs)
    def read
