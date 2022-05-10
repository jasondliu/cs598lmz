import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode="r+", buffering=-1, encoding=None, errors=None, newline=None,
                 closefd=True, opener=None):
        self.__file = io.FileIO(file_path, mode, buffering, encoding, errors, newline, closefd, opener)
        self.__file_name = file_path
        self.__mode = mode
        self.__buffering = buffering
        self.__encoding = encoding
        self.__errors = errors
        self.__newline = newline
        self.__closefd = closefd
        self.__opener = opener
        self.__pos = 0
        self.__file_size = self.__get_file_size()
    def __get_file_size(self):
        if self.name == None:
            return 0
        try:
            return os.path.getsize(self.name)
        except IOError:
            return 0

    def __repr__(self):
        return self.__file.__repr
