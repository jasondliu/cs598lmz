import io
class File(io.RawIOBase):
    def __init__(self, fname):
        self.fname = fname
    def write(self, b):
        f = File(self.fname, "wb")
        f.write(b)
        f.close()
    def readable(self):
        return True
    def read(self, size):
        return b"Hello!"
    def seekable(self):
        return False

import contextlib
@contextlib.contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
with tag('h1'):
    print("foo")

def tag(name):
    def actual_dec(fn):
        @contextlib.contextmanager
        def _tag():
            print("<%s>" % name)
            yield
            print("</%s>" % name)
        return _tag
    return actual_dec
with tag('h1')():
    print("foo")
@tag("i")
def luis():
    print("luis machuca")
