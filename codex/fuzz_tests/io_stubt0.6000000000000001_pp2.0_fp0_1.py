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
view.fill(0)

# test that calling __del__ on an io object does not close the file
# descriptor
with open(io.DEFAULT_BUFFER_SIZE, 'rb') as f:
    f.readinto(view)
    del f
    view.fill(0)
    f = open(io.DEFAULT_BUFFER_SIZE, 'rb')
    f.readinto(view)

# test that calling __del__ on a BufferedReader does not close the file
# descriptor
with open(io.DEFAULT_BUFFER_SIZE, 'rb') as f:
    bf = io.BufferedReader(f)
    bf.readinto(view)
    del bf
    view.fill(0)
    bf = io.BufferedReader(f)
    bf.readinto(view)

# test that calling __del__ on a BufferedWriter does not close the file
# descriptor
with open(io.DEFAULT_BUFFER_SIZE, 'wb') as f:
    bf = io.BufferedWriter(f)
   
