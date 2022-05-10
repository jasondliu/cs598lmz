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

# Test that the file's buffer is also deleted.
gc.collect()
if len(view) != 0:
    raise Exception("Buffer not deleted")
