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

# Issue #16706
import io
import sys

class MyIO(io.TextIOBase):
    def read(self, n=-1):
        return 'x'*n

sys.stdout = MyIO()
