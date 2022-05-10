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

buf = memoryview(bytearray(1))
buf[:] = [42] * 1

print(view[:].tobytes())
