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

# Verify that a weakref to the buffer view still exists
wr = weakref.ref(view)
del view
gc.collect()
assert wr() is not None

# Verify that the raw buffer itself was freed
wr = weakref.ref(view.obj)
del view
gc.collect()
assert wr() is None

# Verify that the weakref to the buffer was freed
wr = weakref.ref(view)
del view
gc.collect()
assert wr() is None

# Verify that the weakref to the file was freed
wr = weakref.ref(f)
del f
gc.collect()
assert wr() is None
