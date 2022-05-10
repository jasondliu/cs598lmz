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

view[0] = ord('x')

# Test that the destructor calls the destructor of the raw object
# (which is an extension type)
#
# This used to segfault when the destructor of the PyFileObject
# was invoked, because the raw object had already been deallocated.

class File(io.RawIOBase):
    def close(self):
        #print("close")
        pass
    def readable(self):
        return True

f = io.BufferedReader(File())
del f
print("ok")
