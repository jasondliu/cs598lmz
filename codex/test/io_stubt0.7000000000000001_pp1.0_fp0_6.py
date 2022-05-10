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

# issue2637
# This test is a bit weird (we're testing the unittest module rather
# than the strptime module), but since it will only trigger when
# strptime is implemented in Python, it has to go here.
try:
    import unittest
except ImportError:
    raise unittest.SkipTest("unittest not found")
