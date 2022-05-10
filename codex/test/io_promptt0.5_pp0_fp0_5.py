import io
# Test io.RawIOBase
try:
    io.RawIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

class MyRawIO(io.RawIOBase):
    def readable(self):
        return True

    def readinto(self, buf):
        return 0

# Test io.BufferedIOBase
try:
    io.BufferedIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

class MyBufferedIO(io.BufferedIOBase):
    def readable(self):
        return True

    def readinto(self, buf):
        return 0

# Test io.TextIOBase
try:
    io.TextIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

class MyTextIO(io.TextIOBase):
    def readable(self):
        return True

    def readinto(self, buf):
        return 0

    def read(self, size=-1):
        return ''

    def readline(self, size=-1):
        return ''

# Test
