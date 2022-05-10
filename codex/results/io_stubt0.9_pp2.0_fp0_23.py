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
bytes(view)

# 'b' is not a valid character for the io.TextIOWrapper constructor
try:
    io.TextIOWrapper(None, 'b')
except ValueError as e:
    print(e)

# Check that the C implementation of io.StringIO doesn't use too much memory
# when the initial size is 0 and data is written with
# .write(buffer_containing_unicode).

# Issue #11468.
import sys
io.StringIO().write(sys.maxunicode*"\u1234")
io.StringIO(sys.maxunicode*"\u1234").getvalue()

# Issue #11463.
import io, collections
io.StringIO("A\nB\nC\n").readlines(5)
io.StringIO("A\nB\nC\n").readlines(50)
# Issue #11733: Test that non-text arguments will not be autodetected.
io.StringIO(b"A\nB\nC\n").readlines(50)
io.
