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

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module.

# This is the same as the previous example, except that the buffer is
# created by the io module
