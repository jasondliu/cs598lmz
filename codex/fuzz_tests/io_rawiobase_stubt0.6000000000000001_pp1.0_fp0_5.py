import io
class File(io.RawIOBase):
    def __init__(self, file=None):
        self.file = file
        self.softspace = 0

    def read(self, n=-1):
        return self.file.read(n)

    def readline(self, length=None):
        return self.file.readline(length)

    def write(self, s):
        self.file.write(s)

    def writelines(self, iterable):
        self.file.writelines(iterable)

    def seek(self, pos, whence=0):
        self.file.seek(pos, whence)

    def tell(self):
        return self.file.tell()

    def flush(self):
        self.file.flush()

    def close(self):
        self.file.close()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
       
