import io
class File(io.RawIOBase):
    """
    A file-like object that writes bytes data to a file.
    :param path: the file path
    :param mode: the file mode
    :param buffering: the buffer size
    """
    def __init__(self, path, mode='wb', buffering=-1):
        self.__fd = os.open(path, mode, buffering)
        super().__init__()

    def close(self):
        os.close(self.__fd)

    def write(self, b):
        os.write(self.__fd, b)

    def fileno(self):
        return self.__fd

    def __del__(self):
        self.close()

class FileObject(io.IOBase):
    """
    A file-like object that writes bytes data to a file.
    :param path: the file path
    :param mode: the file mode
    :param buffering: the buffer size
    """
    def __init__(self, path, mode='wb', buffering=-1):
        self.__fd = os.open(
