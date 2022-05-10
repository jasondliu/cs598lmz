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

print(view)

# io.BufferedReader.readinto() calls io.RawIOBase.readinto()
# which calls io.BufferedReader.readinto1()
# which calls io.BufferedReader.readinto_memview()
# which calls PyBuffer_FillInfo()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_GetBuffer()
# which calls PyObject_
