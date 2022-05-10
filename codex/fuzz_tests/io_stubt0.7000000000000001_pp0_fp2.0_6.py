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

def _fget(self):
    return self._io.read(1)
def _fset(self, val):
    self._io.seek(0)
    self._io.write(bytes(1))

def _fdel(self):
    self._io.seek(0)
    self._io.write(bytes(1))

io.BufferedReader.readinto = _fget
io.BufferedReader.write = _fset
io.BufferedReader.close = _fdel

f = io.BufferedReader(File())
f.readinto()
f.write(3)
f.close()
