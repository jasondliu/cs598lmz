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

# Test that readinto() resets failed over-read state
class FailFile(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b'x' * len(buf)
    def readable(self):
        return True

f = io.BufferedReader(FailFile())
f.read(1)
f.read(2)
print(f.read(1))

# Test that the readinto() fast-path works for short reads
class FailFile(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b'x' * len(buf)
        return 1
    def readable(self):
        return True

f = io.BufferedReader(FailFile())
print(f.read(1))
print(f.read(1))
print(f.read(1))

# Check that in non-blocking mode, we return None when the buffer is empty
# and the delegate is empty.
