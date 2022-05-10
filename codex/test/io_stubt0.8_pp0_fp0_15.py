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

# crash: Attempt to deallocate buffer not owned by the interpreter.
#
# The file object was destroyed, which deallocated its _io.BufferedReader,
# which deallocated the view.  Unfortunately, the Py_buffer struct doesn't
# distinguish between a read-only buffer and a buffer that was allocated by the
# interpreter, so when the view was released the interpreter tried to free
# the buffer.
