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

# Test that the buffer was released
print(view)

# Test that the buffer was not released
del view
try:
    print(view)
except NameError:
    pass
else:
    print("NameError not raised")
