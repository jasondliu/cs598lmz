import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
        self.file = open(*args)
    def close(self):
        self.file.close()
    def read(self, *args, **kwargs):
        return self.file.read(*args, **kwargs)
    def write(self, *args, **kwargs):
        return self.file.write(*args, **kwargs)
    def seek(self, *args, **kwargs):
        return self.file.seek(*args, **kwargs)
    def tell(self, *args, **kwargs):
        return self.file.tell(*args, **kwargs)
    def fileno(self, *args, **kwargs):
        return self.file.fileno(*args, **kwargs)
    def flush(self, *args, **kwargs):
        return self.file.flush(*args, **kwargs)
    def seekable(self, *args, **kwargs):
        return self.file.seekable(*args
