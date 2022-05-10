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
print('ok')
</code>
(And on Python 2, use <code>io.BytesIO</code>, <code>io.BufferedReader</code> and <code>file</code> instead of <code>io.StringIO</code>, <code>io.BufferedReader</code> and <code>io.RawIOBase</code>.)

