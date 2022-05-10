import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        while True:
            try:
                return self.file.read(n)
            except IOError as e:
                if e.errno != errno.EINTR:
                    raise
    def readall(self):
        return b''.join(iter(lambda: self.file.read(io.DEFAULT_BUFFER_SIZE), b''))
    def readable(self):
        return True
    def seekable(self):
        return False
    def writeable(self):
        return False

class StdFile(File):
    def __init__(self, std):
        self.std = std
        self.file = std._file
    def __enter__(self):
        return self.std.__enter__()
    def __exit__(self, *args):
        return self.std.__exit__(*args)

class Std(object):
    def __init__(self, file, name):
        self._file =
