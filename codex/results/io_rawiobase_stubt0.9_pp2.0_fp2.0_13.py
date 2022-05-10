import io
class File(io.RawIOBase):
    def error(self, message):
        raise IOError(message)
    def __init__(self, name="noname"):
        self.__closed = False
        self.__eof = False
        self.__pos = 0
        self.file = None
        if isinstance(name, bytes):
            name = name.decode("utf-8")
        if not isinstance(name, str):
            self.error("invalid filename " + str(type(name)))
        self.name = name
    def __repr__(self):
        return "<_io.File " + self.name + ">"
    def close(self):
        if not self.__closed:
            self.flush()
            self.__pos = 0
            self.__eof = False
            self.file.close()
            self.__closed = True
    def readable(self):
        return True
    def readinto(self, b):
        if self.__closed:
            self.error("tried to read from closed stream")
        buffer = bytearray(b
