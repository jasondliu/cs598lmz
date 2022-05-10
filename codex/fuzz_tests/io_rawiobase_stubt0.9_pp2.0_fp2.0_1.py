import io
class File(io.RawIOBase):
    __filePath = None
    __textPath = None
    __file = None

    def __init__(self, path, textPath):
        self.__filePath = path
        self.__textPath = textPath

        self.__file = open(path, "r+")


    def write(self, str):
        self.__file.write(str)
        self.__file.write("\n")
        self.__file.flush()
        #os.write(str)

    def read(self, bytes = -1):
        return self.__file.read(bytes)

    def close(self):
        self.__file.close()

    def seek(self, offset, when = io.SEEK_SET):
        self.__file.seek(offset, when)

    @property
    def path(self):
        return self.__filePath

    @property
    def textPath(self):
        return self.__textPath

    def readable(self):
        return True

    def writable(self):
        return True
