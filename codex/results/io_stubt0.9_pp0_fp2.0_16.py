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

f = os.fdopen(5, 'rb')
f.read(1)
del f
view[0] = 42


old = sys.stdin
sys.stdin = io.open('/dev/null', 'r')
# try to crash the interpreter
exec('abs(-1)')
sys.stdin = old


# test that duplicating a file descriptor using the `dup()` function
# behaves more-or-less as expected (on POSIX systems at least)
import os
f = open(os.devnull)
fd = f.fileno()  # get file descriptor of os.devnull

f2 = os.fdopen(os.dup(fd))  # open a second reference to os.devnull
f2.close()

f.close()  # file descriptor is closed after f2 is closed
