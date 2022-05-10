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

sys.stdin = open(0, encoding='ascii')
print(repr(view))

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view[:] = buf
        return len(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
view = bytearray(10)
f.readinto(view)
del f

sys.stdin = open(0, encoding='ascii')
print(repr(view))

# Fails with a system error or an infinite loop on CPython, or
# just returns something like b'\xe6\x97\xa5\xe6\x97\xa5' (which
# speaks for itself), or raises RecursionError, or fails with
# a RuntimeError showing what's in the buffer.  All wrong.
view = bytearray(10)
f.readinto(view)
del f

print(repr(view))
