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

r = b"1\x02\x03\x04\x05\x06\x07\x08"

if l == r:
    print('ok')
else:
    print('not ok')
