import io
class File(io.RawIOBase):  # Python 3.x
    '''
    Wraps a file object to give it a name.
    Useful in conjuction with StringIO.
    '''
    def __init__(self, name, mode, f):
        self.__name = name
        self.__mode = mode
        self.__f = f

    def __repr__(self):
        return '<File %r in %s>' % (self.__name, self.__mode)

    def close(self):
        if self.__mode.startswith('w') and self.__f is not None:
            self.__f = None  # don't close underlying file
        else:
            super(File, self).close()

    def writable(self):
        return self.__mode.startswith('w')

    def write(self, b):
        check_can_write(self.__mode)
        return self.__f.write(b)

    def readable(self):
        return self.__mode.startswith('r')

    def read(self, n):
