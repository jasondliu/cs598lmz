import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()
    def open(self):
        self.file = open(self.filename, self.mode)
    def close(self):
        self.file.close()
    def read(self, size):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def seek(self, offset, whence):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def flush(self):
        return self.file.flush()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

class FileWithLogging(File):
    def write(self, data):
        print('Writing {!r}'.format(data))
        return super().write(data)

