import io
class File(io.RawIOBase):
    def __init__(self,filename,fmode):
        self.__file = open(filename,fmode)
        if len(fmode) == 1:
            self.__mode = fmode
        else:
            self.__mode = fmode[0]
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        self.close()
    def readable(self):
        return 'r' in self.__mode
    def writable(self):
        return 'w' in self.__mode or 'a' in self.__mode
    def read(self,n=-1):
        return self.__file.read(n)
    def isatty(self):
        returun self.__file.isatty()
    def write(self,b):
        return self.__file.write(b)
    def fileno(self):
        return self.__file.fileno()
    def close(self):
        return self.__file.close()
    def seek
