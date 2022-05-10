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
del File

class File:
    def write(self, data):
        global view
        view[:] = data
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.write(b'hello world')
del f
del File

class File:
    def writable(self):
        return True
    def write(self, data):
        global view
        view[:] = data

f = io.BufferedRWPair(File(), File())
f.write(b'hello world')
del f
del File

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def writable(self):
        return True
    def write(self, data):
        global view
        view[:] = data

f = io.BufferedRWPair(File(), File())
f.write(b'hello world')
del f
del File
