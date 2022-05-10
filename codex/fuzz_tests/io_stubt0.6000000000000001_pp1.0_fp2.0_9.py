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

import gc
gc.collect()

print(view)

# This test case ensures that the cyclic garbage collector
# does not crash when it encounters an instance of BufferedReader
# which contains an instance of RawIOBase which is not in
# the instance dictionary of BufferedReader.
#
# The first read should not crash Python because the cyclic
# garbage collector should be able to detect that the
# BufferedReader object is still alive, even though it is
# not referenced in the instance dictionary of File.
#
# The second read should crash Python.  The cyclic garbage
# collector should not be able to detect that the BufferedReader
# object is still alive since it is not referenced in the
# instance dictionary of File anymore.
