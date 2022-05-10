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

for i in view:
    print(i)
</code>
This doesn't work because I don't know how to pass a <code>Py_buffer</code> to the <code>view</code> property. I couldn't find another way to convert a <code>Py_buffer</code> to a Python object either.

