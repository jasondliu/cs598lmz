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
gc.collect()
print(view) # Python 3 prints bytearray(b'x'), Python 2 prints 'x'
print(type(view)) # Python 3 prints bytearray, Python 2 prints str
</code>

