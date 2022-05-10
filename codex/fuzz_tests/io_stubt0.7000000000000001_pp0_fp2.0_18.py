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

# some random code to test the view
print(view)
view[0] = 42
print(view)
del view
</code>
This code throws a <code>BufferError</code> when executed.

