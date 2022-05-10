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

# Bug in python 2.2: segfaults on this reallocation when
# the buffer gets released.
chunk = 'A' * 100000
for i in range(2):
    chunk = chunk + chunk
