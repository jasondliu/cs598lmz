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

view[0] = 0

# Now the buffer is invalid, but the buffer object is still alive.

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "strict", True)

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "ignore", False)

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "replace", False)

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "surrogateescape", False)

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "surrogatepass", False)

# The following should not crash:
import _io
_io._test_decode_utf8("", 1, "strict", False)

# The following should not crash:
import _io
_io._test_decode_utf8
