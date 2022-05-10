import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

class Output:
    buf = None
    def write(self, data):
        global view
        view = data

o = Output()
f = io.TextIOWrapper(io.BufferedWriter(o))
f.write('x')
del f
del o

class Output:
    buf = None
    def write(self, data):
        global view
        view = data

o = Output()
f = io.TextIOWrapper(o)
f.write('x')
del f
del o

# Test that unicode errors can be overridden with a custom error handler
def bad_handler(exc):
    raise exc

f = io.TextIOWrapper(io.BytesIO(b'\xc0'), encoding='ascii', errors='strict')
f.read()
f.errors = bad_handler
f.read()

# Test that TextIOWrapper with a buffer larger than 1 byte correctly
# handles a replacement character that is split across two buffer
# loads.
f = io.TextIOWrapper(io.Bytes
