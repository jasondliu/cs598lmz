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

buf = memoryview(view)
buf[0] = 0
buf[0] = 1
buf[1] = 2
buf[0] = 3
buf[1] = 4
buf[0] = 5
buf[1] = 6
buf[0] = 7
buf[1] = 8
buf[0] = 9
buf[1] = 10
buf[0] = 11
buf[1] = 12
