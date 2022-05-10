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
gc.collect()
print(view)

# TODO:
#  - test that it does not crash with a subclass of io.RawIOBase
#  - test that it does not crash with io.BytesIO
#  - test that it does not crash with io.StringIO
#  - test that it does not crash with io.BufferedReader
#  - test that it does not crash with io.BufferedWriter
#  - test that it does not crash with io.BufferedRWPair
#  - test that it does not crash with io.BufferedRandom
#  - test that it does not crash with io.TextIOWrapper
#  - test that it does not crash with io.FileIO
#  - test that it does not crash with io.BytesIO
#  - test that it does not crash with io.TextIOBase
#  - test that it does not crash with io.IOBase
#  - test that it does not crash with io.RawIOBase
