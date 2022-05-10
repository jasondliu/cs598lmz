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

# make sure that the buffer is not freed
print(len(view))

# make sure that the buffer is not freed
# (this will crash if the buffer is freed)
view[0] = 0

print("ok")
