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
buf = view
for i in range(len(buf)):
    buf[i] = 0x41
