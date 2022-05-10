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
f.read(0)
f.read()
f.read(10)
f.read(1024)
f.close()
f.closed

fp = io.BufferedReader(io.BytesIO(b"abcdefg"))
fp.seek(0)
fp.read(5)
fp.read(1)
fp.read()
fp.seek(-1, io.SEEK_CUR)
fp.read(1)
fp.seek(-1, io.SEEK_END)
fp.read(1)
fp.seek(0)
fp.read(1024)
fp.seek(0)
fp.read(3)
fp.read(1024)
fp.seek(0)
fp.read()
fp.seek(0)
fp.read(None)
fp.seek(0)
fp.readinto(bytearray(10))
fp.seek(0)
