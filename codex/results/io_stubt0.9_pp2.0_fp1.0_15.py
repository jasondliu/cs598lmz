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
buf = view  # objective: supress warning
</code>
is it possible to have separate warnings per instance even though they have the same type?

