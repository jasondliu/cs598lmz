import io
class File(io.RawIOBase):
    """
    A file-like object that reads from a `.tar` file.

    This is a file-like object that reads from a `.tar` file. It is
    intended to be used with `tarfile.open()` as a `mode` argument.

    """

    def __init__(self, name, mode="r", fileobj=None, bufsize=10240):
        if mode not in ("r", "w", "r|", "w|", "a", "a|"):
            raise ValueError("mode must be 'r', 'w', 'r|', 'w|', 'a' or 'a|'")
        self.name = name
        self.mode = mode
        self.closed = False
        self.offset = 0
        self.bufsize = bufsize
        self.filesize = 0
        self.fileobj = fileobj
        self.pos = 0

        if fileobj is None:
            fileobj = io.FileIO(name, mode)
        self.fileobj = fileobj

    def read(self, size=-1):
       
