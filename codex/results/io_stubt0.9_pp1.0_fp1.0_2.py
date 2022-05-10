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
sys.stdout.buffer.write(view)
</code>
It will show you the underlying Python3 string buffer for the <code>sys.stdout</code> instance.

