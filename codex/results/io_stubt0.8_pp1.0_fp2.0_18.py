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

a = bytearray(b'abc')
a[1] = b'\xff'
print(view)
print(a)
</code>
Output:
<code>bytearray(b'a\xffc')
bytearray(b'a\xffc')
</code>

