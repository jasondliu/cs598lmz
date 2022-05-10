fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Avoid crashes in _PyObject_GC_TRACK / _PyObject_GC_UNTRACK
class C:
    def __init__(self):
        self.__dict__ = self
        self.__dict__ = None
        self.__dict__ = self
C()

# Issue #9279: don't crash when deallocating a weakref to an object
# that defines __del__
class C:
    def __del__(self):
        pass
import weakref
weakref.ref(C())

# Issue #9284: don't crash when hashing an object with a bad __hash__
# method.
import sys
class C:
    def __hash__(self):
        raise ValueError
    def __eq__(self, other):
        raise RuntimeError
try:
    hash(C())
except ValueError:
    pass
# In Python 3, __eq__ is ignored when __hash__ raises an exception.
# In Python 2, the exception propagates.
if sys.version_info[0] >= 3:
    try:

