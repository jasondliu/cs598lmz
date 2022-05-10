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
del view
gc.collect()
# The file object should now be destroyed.  Check that the buffer is
# also destroyed.  This is done by looking at the destructor count
# in sys.gettotalrefcount().
start = sys.gettotalrefcount()
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
del view
gc.collect()
new = sys.gettotalrefcount()
if new != start:
    print("destructor count not restored")
