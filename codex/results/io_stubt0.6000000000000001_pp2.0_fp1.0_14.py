import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, view
</code>
(You can also use <code>io.BufferedReader.peek</code> or <code>io.BufferedReader.read1</code>, but neither of those lets you control how much data is read.)

