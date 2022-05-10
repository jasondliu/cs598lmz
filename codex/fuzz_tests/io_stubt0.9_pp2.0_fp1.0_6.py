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
# bad results from this point on; buf should have been deallocated
# on f's destruction, but wasn't.  See issue #20825.
# The _PyIO_ReleaseBuffers() call (when buf is attached to f)
# didn't deallocate buf.
print(sys.getallocatedblocks())
print(sys.getallocatedblocks() == view)
