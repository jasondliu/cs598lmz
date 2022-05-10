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
sys.getrefcount(view)

# BUG: my stdout is unbuffered and the buffering code still sometimes tries
# to use it, giving 'TypeError: unicode argument expected, got 'str''
