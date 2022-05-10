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
f = io.BufferedReader(File())
f.read(1)

class FileWithClose(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 0
    def readable(self):
        return True
    def close(self):
        pass

f = io.BufferedReader(FileWithClose())
f.read(1)
del f
f = io.BufferedReader(FileWithClose())
f.read(1)
