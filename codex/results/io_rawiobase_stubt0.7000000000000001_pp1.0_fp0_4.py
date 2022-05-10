import io
class File(io.RawIOBase):
    def close(self):
        return super().close()
    def fileno(self):
        return super().fileno()
    def flush(self):
        return super().flush()
    def isatty(self):
        return super().isatty()
    def readable(self):
        return super().readable()
    def readline(self, size=-1):
        return super().readline(size)
    def readlines(self, hint=-1):
        return super().readlines(hint)
    def seek(self, offset, whence=io.SEEK_SET):
        return super().seek(offset, whence)
    def seekable(self):
        return super().seekable()
    def tell(self):
        return super().tell()
    def truncate(self, size=None):
        return super().truncate(size)
    def writable(self):
        return super().writable()
    def write(self, b):
        return super().write(b)
    def writelines(self, lines):
        return super().writelines(lines
