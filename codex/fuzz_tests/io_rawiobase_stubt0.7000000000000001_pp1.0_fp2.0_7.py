import io
class File(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readline(self, limit=-1):
        pass
    def readlines(self, hint=-1):
        pass
    def fileno(self):
        return 0
    def truncate(self, size=None):
        pass
    def write(self, b):
        pass
    def writelines(self, lines):
        pass
    def flush(self):
        pass
    def isatty(self):
        return False


class BufferedReader(io.BufferedIOBase):
    def readable(self):
        return True
    def seekable(self):
        return True
    def read(self, size=-1):
        pass
    def read1(self, size=-1):
        pass
    def readinto(self, b):
        pass
    def readinto1(self, b):
        pass
    def readline(self, limit=-1):
        pass
    def peek(self, size
