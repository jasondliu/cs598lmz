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

view[0] = 0

# The following line should crash the interpreter.
# If it does not, it means that the GC did not
# collect the File object.
print(view[0])
