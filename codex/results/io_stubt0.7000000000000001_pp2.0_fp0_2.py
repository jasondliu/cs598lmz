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
view

class File(io.RawIOBase):
    def readinto(self, buf):
        global bview
        bview = bytes(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
bview

# Test __sizeof__
__sizeof__(io.BytesIO())
io.BytesIO().__sizeof__()
import sys
__sizeof__(io.BytesIO()) >= sys.getsizeof(io.BytesIO())

class MyBytesIO(io.BytesIO):
    pass

__sizeof__(MyBytesIO())
__sizeof__(io.StringIO())

# Test readline()

# Test readlines()

# Test writelines()

# Test truncate()

# Test fileno()

# Test isatty()

# Test close()

# Test detached()

# Test newlines

# Test line buffering

# Test mix of read() and readline()

# Test readline() after seek
