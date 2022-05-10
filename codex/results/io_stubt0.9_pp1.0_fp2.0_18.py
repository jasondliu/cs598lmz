import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
# show buffer object
view

# with statement: RAII
with File() as f:
    f.read(1)

# context manager: two methods / functions
# __enter__: returns __enter__ value or yields from a generator
# __exit__: returns True to suppress exception or False otherwise
class File:
    def close(self):
        super().close()  # call client close method
        f = self.__dict__['f']
        f.close()  # close underlying file
    def isatty(self):
        f = self.__dict__['f']
        return f.isatty()
    def __init__(self, name, mode='r', *, encoding=None, newline=None):
        self.__dict__['f'] = open(name, mode, newline=newline)
        if encoding:
            self.__dict__['f'] = io.TextIOWrapper(self.__dict__['f'],
                                                  encoding=encoding)

    def __iter__(self):
        f = self.__dict__
