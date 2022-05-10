import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="rb", closefd=True):
        self.name = filename
        self.mode = mode
        self.closefd = closefd
        self._fd = io.open(filename, mode, closefd=closefd)
        self.length = self._fd.seek(0, io.SEEK_END)
        self._fd.seek(0)
    def fileno(self):
        return self._fd.fileno()
    def seekable(self):
        return True
    def seek(self, offset, whence):
        return self._fd.seek(offset, whence)
    def read(self, size):
        return self._fd.read(size)
    def readable(self):
        return True
    def write(self, data):
        return self._fd.write(data)
    def writable(self):
        return True

class FileSystem(object):
    def __init__(self):
        self.filesystem = []
        self.filesystem.append(File("testdata/filedata"))
       
