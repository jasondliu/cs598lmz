import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='rb'):
        self.__file = None
        self.__file_path = file_path
        self.__mode = mode
        self.__file_size = os.path.getsize(self.__file_path)
        self.__current_position = 0
        self.__is_closed = False
        self.__file = open(self.__file_path, mode)

    def close(self):
        if self.__file:
            self.__file.close()
            self.__file = None
        self.__is_closed = True

    def fileno(self):
        return self.__file.fileno()

    def flush(self):
        self.__file.flush()

    def isatty(self):
        return self.__file.isatty()

    def readable(self):
        return self.__mode in ('r', 'r+', 'rb', 'rb+', 'rw', 'rw+')

    def readline(self, size=-1):
        return
