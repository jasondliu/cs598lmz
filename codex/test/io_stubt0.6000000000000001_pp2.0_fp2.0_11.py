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

# The following code is a test for a bug that was fixed in CPython 3.6.
# After the bug was fixed, the following code does not cause a segfault.
#
# This test is a modified version of test_io.test_bad_readinto()

class MyFile(io.RawIOBase):
    def readable(self):
        return True

f = MyFile()
