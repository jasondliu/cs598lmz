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

gc.collect()

if view:
    print("*" * 100)
    print("Memory leak detected")
    print("*" * 100)
else:
    print("No memory leak detected")
