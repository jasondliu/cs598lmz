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

# This should not blow up in the destructor
del view

# Now we check that the destructor does not blow up when the view is
# resized.
