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

def g():
    yield

try:
    g().close()
except AttributeError:
    print("SKIP")
    raise SystemExit

# test that CPython's custom buffered I/O objects don't have the
# __next__ method, which the bufferedio module doesn't support
try:
    next(io.BytesIO())
except TypeError:
    print('TypeError')
except AttributeError:
    print('AttributeError')
