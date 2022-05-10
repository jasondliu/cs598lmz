import io
class File(io.RawIOBase):
    """ Wraps a file so we get fileno() """
    def __init__(self, file):
        if isinstance(file, str):
            self.file = open(file, "rb")
        else:
            self.file = file
        self.closed = False
        self.rptr = 0

    #
    # These functions are primarily used if we are passed a string.  But
    # ultimately all the functions should be supported as we are trying
    # to act as a drop in for io.RawIOBase for the most part.
    #

    def write(self, b):
        pass

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        l = len(b)
        tmp = self.read(l)
        b = tmp
        return l

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        self
