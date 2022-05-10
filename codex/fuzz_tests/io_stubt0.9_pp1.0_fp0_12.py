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
buf = b'a'*128
del buf
gc.collect()

# The above create a chain of references from the _io.BufferedReader object to the file object
# to a bytearray, which is not optimized at the C level, to a memoryview, internally managed
# by the _io module, to the internal buffer of our dying bytearray, the only reference to this
# bytearray.  This chain prevents the bytearray from being freed, which causes a memory leak,
# which causes a ResourceWarning.

# However, at the time of writing, the reference count of the PyObject associated to the
# memoryview is not decremented at all during the destruction of the _io.BufferedReader
# object, so the bytearray is not freed and the chain of references isn't destroyed.
# But a user will see a ResourceWarning anyway because the PyObject's garbage collection
# flag is set to 0 instead of 1, and the memoryview is never deallocated.
#
# The PyObject is not deallocated because the internal _PyGC_FINALIZED
