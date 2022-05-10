import io
class File(io.RawIOBase):
    """
    A file-like object that writes to a file descriptor.
    """
    def __init__(self, fd):
        self._fd = fd

    def close(self):
        return os.close(self._fd)

    def fileno(self):
        return self._fd

    # RawIOBase methods
    def readinto(self, b):
        return os.read(self._fd, b)

    def write(self, b):
        return os.write(self._fd, b)

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return False


def simple_reader_writer(fd):
    """
    Return a tuple of reader, writer where each is a file-like object
    for the given file descriptor.

    Use this function to get reader/writer objects when you don't need
    to do any extra buffering.
    """
    return File(fd), File(fd)


def reader(fd):
    """
    Return a file-like object for
