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

# it looks like CPython 3.2+ allows this, but PyPy doesn't
#import gc
#gc.collect()

print(view)
</code>

