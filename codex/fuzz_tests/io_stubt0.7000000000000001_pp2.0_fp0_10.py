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

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint8)]
v = V.from_buffer(view)
v.a = 255
del v
print(view)
