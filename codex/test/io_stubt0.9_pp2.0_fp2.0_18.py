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
str(view)

# Test that when a BufferedReader has a small initial bytearray, the effect
# of mark() is that the next time read() is called, the user will get their
# data back. On the other hand, we test that if mark() is called twice in a row
# (and therefore a larger bytearray is allocated), the "memory" is scrambled.

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b"hello, world"
        self.count += 1
        return len(buf)
    def readable(self):
        return True

f = io.BufferedReader(File(), 1)
f.count = 0

