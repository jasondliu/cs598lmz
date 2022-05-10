import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, File

class NewFile(io.RawIOBase):
    def readinto(self, buf):
        # buf[:] = b""
        buf[:] = b"123456789"
    def readable(self):
        return True

f = io.BufferedReader(NewFile())
