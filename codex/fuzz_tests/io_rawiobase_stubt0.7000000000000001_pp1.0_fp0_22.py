import io
class File(io.RawIOBase):
    """Dummy file object.

    This class implements the RawIOBase API, but does not actually write or
    read anything. It is intended for testing purposes.
    """
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return len(b)
    def write(self, b):
        return len(b)
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0

class FileIO(io.RawIOBase):
    """Raw I/O implementation for file objects.

    This class supports the makefile() method on file objects.
    """
    def __init__(self, file, mode):
        if mode not in ('r', 'w', 'x', 'a', 'r+', 'w+', 'x+', 'a+', 'rb', 'wb',
                        'xb', 'ab', 'r+b', 'w+b', 'x+b', 'a+
