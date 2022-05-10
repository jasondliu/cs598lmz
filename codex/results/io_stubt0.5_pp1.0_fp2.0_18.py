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

# CPython:
#   malloc(1)
#   free(1)
# PyPy:
#   malloc(1)
#   malloc(1)
#   free(1)
#   free(1)
#
# This is because the buffer inside BufferedReader is not
# released when the BufferedReader is deleted.
#
# It is not clear how to fix this without breaking other
# tests.
