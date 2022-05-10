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
print('a', end='')
print('b', end='')
print('c')
print('d', end='')
print('e', end='')
print('f')

# Issue #16709
import io

class MyIO(io.TextIOBase):
    def read(self, n=-1):
        return 'x'*n
    def readline(self, n=-1):
        return 'x'*n

sys.stdout = MyIO()
print('a', end='')
print('b', end='')
print('c')
print('d', end='')
print('e', end='')
print('f')

# Issue #16710
import io

class MyIO(io.TextIOBase):
    def read(self, n=-1):
        return 'x
