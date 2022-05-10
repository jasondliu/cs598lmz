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

class File:
    def write(self, text):
        global read
        read = text
    def writable(self):
        return True

f = io.BufferedWriter(File())
