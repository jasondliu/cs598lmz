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

# This is a test for a bug in the io module.  The bug is that
# io.BufferedReader.readinto() does not call the underlying
# RawIOBase.readinto() method.  Instead, it calls RawIOBase.read()
# and then copies the result into the buffer.  This is inefficient,
# and in some cases (such as this one) it can cause the program to
# crash.

# The bug is in the C code, so it's not easy to fix.  The workaround
# is to use io.BufferedReader.read() instead of readinto().  This
# has the advantage that it also works on Python 2.6 and earlier.

# This test is based on a bug report by Tadek Pietraszek.
