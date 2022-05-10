import io
class File(io.RawIOBase):
    def __init__(self, file_):
        self.file = file_
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        self.file.write(b)
    def flush(self):
        self.file.flush()
    def seekable(self):
        return self.file.seekable()
    def seek(self, *args):
        self.file.seek(*args)
    def tell(self):
        return self.file.tell()
    def fileno(self):
        return self.file.fileno()
    def close(self):
        self.file.close()
    def readable(self):
        return self.file.readable()
    def writable(self):
        return self.file.writable()

class FileWrapper(File):
    def __init__(self, file_, wrapper):
        super(FileWrapper, self).__init__(file_)
        self.wrapper = wrapper
    def read(self, size=-1):

