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
try:
    view[0] = 1
except:
    print("SKIP")
    raise SystemExit

# io.RawIOBase.readinto() must return None
f = io.BufferedReader(io.BytesIO(b'abc'))
buf = bytearray(b'x'*3)
print(f.readinto(buf))
