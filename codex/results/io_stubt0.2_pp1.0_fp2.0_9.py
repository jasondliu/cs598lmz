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

# This is a bit tricky.  We want to make sure that the buffer
# is not freed before the file is closed.  The file is closed
# when the reference count of the file object drops to zero.
# The buffer is freed when the reference count of the buffer
# object drops to zero.  So we create a reference cycle
# between the file and the buffer.  The reference cycle is
# broken when the file is closed.  The buffer is freed when
# the reference count of the buffer object drops to zero.
# The reference count of the buffer object drops to zero
# when the reference count of the file object drops to zero.
# The reference count of the file object drops to zero when
# the reference count of the buffer object drops to zero.
# The reference count of the buffer object drops to zero
# when the reference count of the file object drops to zero.
# The reference count of the file object drops to zero when
# the reference count of the buffer object drops to zero.
# The reference count of the buffer object drops to zero
# when the reference count of the file object drops to zero.
# The reference count of the file
