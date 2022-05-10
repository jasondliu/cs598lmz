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

import gc; gc.collect()

buf = bytearray(1)
memoryview(buf)[:]
view[:]

# This used to crash the interpreter due to a double free caused by
# the decref the PyObject_Free call in the memoryview call
