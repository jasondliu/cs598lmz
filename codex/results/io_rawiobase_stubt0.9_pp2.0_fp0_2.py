import io
class File(io.RawIOBase):
    def __init__(self, fh):
        self.fh = fh
        self.mode = fh.mode
        self.closefcn = fh.close
    def read(self, n=-1):
        return self.fh.read(n)
    def seekable(self):
        return True
    def readable(self):
        return True
    def seek(self, pos, whence=0):
        if whence != 0 or pos != 0:
            raise ValueError("invalid argument")
        self.fh.seek(0, 0)

f = open("hello.txt", "rb")
fdetach = File(f)
fdetach.read(5)

class MyFile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fh = None

    def __enter__(self):
        self.fh = open(self.filename, self.mode)
        return self.fh

    def __exit__(self, exc_type,
