import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self.file = self._open(filename, mode)

    def close(self):
        return self.file.close()

    def read(self, n=-1):
        return self.file.read(n)

    def seek(self, pos, whence=0):
        return self.file.seek(pos, whence=0)

    def tell(self):
        return self.file.tell()

    def write(self, b):
        return self.file.write(b)

class FileProxy(File):
    def _open(self, filename, mode):
        return open(filename, mode)

class FileBackup(File):
    def _open(self, filename, mode):
        if mode.startswith('r'):
            return open(filename + '.bak', mode)
        else:
            return open(filename, mode)

def load_file(filename, mode='r', proxy=False):
    if proxy:
        file = FileProxy(filename, mode)
    else
