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

x = view[0]
if x == int.from_bytes(b'X', sys.byteorder):
    print('PASS')
else:
    print('FAIL: Expected X, got {}'.format(x))
</code>
but it is still not enough.

