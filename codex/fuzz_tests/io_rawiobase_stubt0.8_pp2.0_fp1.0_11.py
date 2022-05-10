import io
class File(io.RawIOBase):
    def readall(self):
        return self.read()
    def readline(self):
        raise NotImplementedError()
    def writelines(self, lines):
        for line in lines:
            self.write(line)
    def seekable(self):
        return 0
    def __iter__(self):
        return self
    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line
    def tell(self):
        raise io.UnsupportedOperation("tell")

class GzipFile(File):
    """The GzipFile class simulates most of the methods of a file object with
    the exception of the readinto() and truncate() methods.
    """

    def __init__(self, filename=None, mode=None,
                 compresslevel=9, fileobj=None, mtime=None):
        """Constructor for the GzipFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is
