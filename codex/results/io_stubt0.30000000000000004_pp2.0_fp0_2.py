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

view[0] = ord('a')

# test that the buffer is not deallocated
view[0] = ord('b')

# test that the buffer is not deallocated
view[0] = ord('c')

# test that the buffer is not deallocated
view[0] = ord('d')

# test that the buffer is not deallocated
view[0] = ord('e')

# test that the buffer is not deallocated
view[0] = ord('f')

# test that the buffer is not deallocated
view[0] = ord('g')

# test that the buffer is not deallocated
view[0] = ord('h')

# test that the buffer is not deallocated
view[0] = ord('i')

# test that the buffer is not deallocated
view[0] = ord('j')

# test that the buffer is not deallocated
view[0] = ord('k')

# test that the buffer is not deallocated
view[0] = ord('l
