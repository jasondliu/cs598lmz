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

# Generate a string
print(view[:])
# Generate a string
print(view[:])

# Generate a bytes object
print(bytes(view))
# Generate a bytes object
print(bytes(view))

# Generate a bytearray object
print(bytearray(view))
# Generate a bytearray object
print(bytearray(view))
