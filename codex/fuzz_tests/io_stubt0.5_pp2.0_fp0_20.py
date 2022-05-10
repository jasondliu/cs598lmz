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

# print(view)

# import ctypes
# ctypes.string_at(id(view), 1)

# ctypes.string_at(id(view), 1)

# import ctypes
# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# import ctypes
# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove(id(view), b"a", 1)

# ctypes.memmove
