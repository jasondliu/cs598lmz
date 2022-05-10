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

def gc_collect():
    for i in range(10):
        _ = gc.collect()

# Force a GC collection before the test.  This is needed because we
# changed the gc module, so the auto-collect feature doesn't work.
gc_collect()

# This should not segfault.
gc_collect()
