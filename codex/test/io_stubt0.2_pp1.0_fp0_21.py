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

# Test that the buffer is not deallocated when the file is closed.
# This is a regression test for http://bugs.python.org/issue12072
view[0] = 0

# Test that the buffer is not deallocated when the file is garbage collected.
# This is a regression test for http://bugs.python.org/issue12072
del f
gc.collect()
view[0] = 0

# Test that the buffer is not deallocated when the file is closed.
# This is a regression test for http://bugs.python.org/issue12072
f = io.BufferedReader(File())
f.read(1)
del f
view[0] = 0

# Test that the buffer is not deallocated when the file is garbage collected.
# This is a regression test for http://bugs.python.org/issue12072
del f
gc.collect()
view[0] = 0

# Test that the buffer is not deallocated when the file is closed.
# This is a regression test for http://bugs.python.org/issue12
