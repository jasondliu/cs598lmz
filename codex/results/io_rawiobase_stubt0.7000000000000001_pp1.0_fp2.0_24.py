import io
class File(io.RawIOBase):
    pass

f = File()
f.raw is f
#True

f.raw is f.__enter__()
#True

class File():
    def read(self, n=-1):
        return "read"

    def write(self, s):
        pass

    def close(self):
        pass
f = File()
f.read()
#'read'
f.read(10)
#'read'
f.read1(10)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'File' object has no attribute 'read1'

class File():
    def __init__(self):
        self.is_open = False

    def open(self, filename, mode):
        self.is_open = True

    def read(self, n=-1):
        return "read"

    def write(self, s):
        pass

    def close(self):
        self.is_open = False

    def __enter__(self):
        if not
