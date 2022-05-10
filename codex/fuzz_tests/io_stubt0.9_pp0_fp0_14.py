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
view.release(0)

class File(io.RawIOBase):
    def readline(self, limit=-1):
        return "".encode()
    def readable(self):
        return True

f = io.BufferedReader(File())
del f

class File(io.RawIOBase):
    def read(self, size=-1):
        return "".encode()
    def readable(self):
        return True

f = io.BufferedReader(File())
del f
f = None
del f

# Issue 5445: LineBufferedWriter.close() should flush all lines.
# Otherwise it could lead to infinite loops and SystemError: can't set
# exceptions on integer objects.
f = io.BytesIO()
for i in range(100):
    f.write(b'hello\n' * 100)
f.seek(0)
f = io.BufferedReader(io.BufferedReader(f))
f = io.TextIOWrapper(f, line_buffering=True)
f.read(5)
f.close
