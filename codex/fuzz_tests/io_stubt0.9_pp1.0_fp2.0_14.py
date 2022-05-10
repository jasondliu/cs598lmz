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

# This can fail in many ways, but if it fails, it should just
# print an error message and exit.
print(view)
 
# The output should be the same as the original file's.
