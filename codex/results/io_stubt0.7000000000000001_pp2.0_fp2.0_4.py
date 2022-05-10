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

class File2(io.RawIOBase):
    def readable(self):
        return True

try:
    f = io.BufferedReader(File2())
    f.read(1)
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test that a view is not made a long-lasting reference to the wrapped
# object, if it's not necessary.
class File3(io.RawIOBase):
    def readinto(self, buf):
        self.mybuf = buf
    def readable(self):
        return True

f = io.BufferedReader(File3())
f.read(1)
del f
gc.collect()
view = None
# If the view was kept alive, it would still be holding a reference to
# File3, so it would not be collected, and it would hold on to buf.
if gc.collect():
    print("unreachable objects found")

# Test that with line buffering, an extra newline is returned at the end
# of the file.
class File4(io.Raw
