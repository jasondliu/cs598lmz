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

# Verify that the view is still alive.
print(view)

# This used to crash because the buffer was not correctly cleared in the
# destructor of the BufferedReader.
del view

print("OK")
