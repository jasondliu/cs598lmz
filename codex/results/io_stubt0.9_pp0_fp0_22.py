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
</code>
A possible workaround is to create the <code>f</code> in a function and return it, so it will be destroyed when going out of scope.
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

def get_file():
    return io.BufferedReader(File())

f = get_file()
f.read(1)
</code>

