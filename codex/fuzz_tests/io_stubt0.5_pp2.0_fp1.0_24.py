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

# This is a regression test for a bug in the garbage collector.  It
# failed with a RuntimeError: deallocating None.
#
# The bug was that the finalizer for the io.BufferedReader instance
# (f) was invoked with f set to None.  The finalizer called
# f.raw.close(), and f.raw was also set to None.  The weakref to f
# was not cleared until after the finalizer had run, so the
# finalizer was run again, this time with f.raw set to None.  The
# second time through the finalizer, the weakref to f was cleared,
# but the weakref to f.raw was not.  The next time the garbage
# collector ran, it tried to call the finalizer for f.raw, which was
# None, causing the exception.

# This test is a variation of test_io.  The difference is that the
# finalizer for the io.BufferedReader instance (f) is invoked with
# f set to None.  The finalizer calls f.raw.close(), and f
