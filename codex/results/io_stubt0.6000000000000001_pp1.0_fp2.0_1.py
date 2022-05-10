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
print(view)

# If BufferedReader has no buffer, it uses an internal buffer of size 1
# (test_small_buffer)
#
# We assume that if the underlying object is an instance of File, it
# will never return more than 1 byte at a time.

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[0] = 42
        return 1
    def readable(self):
        return True

f = io.BufferedReader(File())
print(f.read(1))
del f

# If BufferedReader has no buffer, it uses an internal buffer of size 1
# (test_small_buffer)
#
# We assume that if the underlying object is an instance of File, it
# will never return more than 1 byte at a time.

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[0] = 42
        return 1
    def readable(self):
        return True

f = io.BufferedReader(File())
print(f.read(1
