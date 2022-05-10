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
del view

# Issue #6997: Reference cycle involving __class__ and __bases__
# attributes
#
# See also test_gc.py:CycleWithGeneratorAndDict.
class C:
    pass
