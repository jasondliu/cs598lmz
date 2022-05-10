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
del view
gc.collect()

del foo
gc.collect()

w("holes: " + stdlib.sys.getsizeof(foo))
gc.collect()
w("holes: " + stdlib.sys.getsizeof(foo))
