import io
class File(io.RawIOBase):
    """
    перенести в отдельный модуль 
    """
    def __init__(self, path: str, mode: str="r"):
        self._file = open(path, mode)
    def read(self, size=-1):
        return self._file.read(size)
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hintsize=None):
        return self._file.readlines(hintsize)
    def write(self, b):
        return self._file.write(b)
