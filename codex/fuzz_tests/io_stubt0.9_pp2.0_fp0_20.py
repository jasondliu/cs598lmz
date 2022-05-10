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

view[0] = b'1'

class FileBase(io.RawIOBase):
    def fileno(self):
        return sys.getfilesystemencoding()

class FileOne(FileBase):
    def write(self, b):
        global buf
        buf = b.decode('ascii')
    def writable(self):
        return True

class FileTwo(FileBase):
    def readinto(self, b):
        return 1
    def readable(self):
        return True

io.open(FileOne())
io.open(FileTwo())
