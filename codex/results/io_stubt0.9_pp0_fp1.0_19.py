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
del File
# buf will be the same as view, so...
assert buf is view

# ...they must point to the same byte_buffer
assert byte_buffer is buf.obj
del buf

# ...at this point there is only one reference to the byte_buffer: view, so...
del byte_buffer
del view

# ...now...
assert 0, "We should never get here"
