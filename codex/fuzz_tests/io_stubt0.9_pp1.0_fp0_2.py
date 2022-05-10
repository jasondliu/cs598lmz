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

memoryview(b'123')
#f = open('testfile', 'rb')
#s = memoryview(f.read())
#del s
#f.close()
