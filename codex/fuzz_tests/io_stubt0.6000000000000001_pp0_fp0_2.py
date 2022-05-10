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
buf[0] = ord('s')
buf[1] = ord('p')
buf[2] = ord('a')
buf[3] = ord('m')
buf[4] = 0

print(view)
