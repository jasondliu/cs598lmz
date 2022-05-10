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

view[0] = 0

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it is garbage collected
f = io.BufferedReader(File())

# create a new file object, which will be freed when it
