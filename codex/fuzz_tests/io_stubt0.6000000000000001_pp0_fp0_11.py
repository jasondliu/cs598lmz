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
C.__class__ = C
C.__bases__ = (C,)

# Issue #7135: Reference cycles involving __weakref__
#
# See also test_gc.py:CycleWithWeakrefAndDict.
class D:
    pass
def fn():
    d = D()
    d.d = d
    d.__weakref__ = weakref.ref(d)
    return d

# Issue #7183: Reference cycles involving __getattr__
#
# See also test_gc.py:CycleWithGetattrAndSetattr.
class E:
    def __getattr__(self, name):
        return self

# Issue #12057: Reference cycles involving __del__
#
# See also test_gc.py:CycleWithDel.
class F:
    def __del__(self):
        pass
