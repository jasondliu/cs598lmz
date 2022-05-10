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

# Test io.BufferedReader.__enter__(), io.BufferedReader.__exit__()
# with __enter__ returning self.
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
with f as f2:
    f2.read(1)
del f
view

# Test io.BufferedReader.__enter__(), io.BufferedReader.__exit__()
# with __enter__ not returning self.
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
with f as f2:
    pass
del f
view

# Test io.BufferedReader.peek
import io

class File(io.RawIOBase):
    def readinto(self, buf):
       
