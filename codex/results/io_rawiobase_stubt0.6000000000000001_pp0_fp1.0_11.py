import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode):
        self.file = open(file_path, mode)
        self.mode = mode
        self.name = file_path
        self.closed = False
        self.pos = 0

    def close(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        self.file.close()
        self.closed = True

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return self.mode in ["r", "r+", "rb", "rb+"]

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if whence == io.SEEK_SET:
            self.pos = offset
        elif whence == io.SEEK_CUR:
            self.
