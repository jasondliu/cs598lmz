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
assert view == memoryview(b'\x00')
del view

class File2(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 0
    def readable(self):
        return True

f = io.BufferedReader(File2())
f.read(1)
del f
assert view == memoryview(b'')

class File3(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 1
    def readable(self):
        return True

f = io.BufferedReader(File3())
f.read(1)
del f
assert view == memoryview(b'\x00')

class File4(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 1024
    def readable(self):
        return True

f = io.BufferedReader(File4())
f.read(1)
del f
assert view == memoryview(b'
