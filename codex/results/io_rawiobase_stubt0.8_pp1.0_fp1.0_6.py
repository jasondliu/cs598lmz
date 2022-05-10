import io
class File(io.RawIOBase):
    pass

class FileIO(io.FileIO):
    pass

class BytesIO(io.BytesIO):
    pass

class BufferedReader(io.BufferedReader):
    pass

class TextIOWrapper(io.TextIOWrapper):
    pass

class UnsupportedOperation(io.UnsupportedOperation):
    pass

class LineIterator(io.IOBase):
    pass

@__extend__(io.IOBase)
class IOBase:
    def fileno(self):
        return self.__getrawfile__().fileno()
    def close(self):
        return self.__getrawfile__().close()
    def flush(self):
        return self.__getrawfile__().flush()
    def read(self, size=-1):
        return self.__getrawfile__().read(size)
    def readline(self, size=-1):
        return self.__getrawfile__().readline(size)
    def readable(self):
        return self.__getrawfile__().readable()
    def
