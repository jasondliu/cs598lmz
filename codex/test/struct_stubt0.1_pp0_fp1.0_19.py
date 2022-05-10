from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError:
    print('TypeError')

# Issue #17077: segfault with __new__ returning NULL
import _testcapi
class C(_testcapi.WithAcquireRelease):
    def __new__(cls):
        return None

try:
    C()
except TypeError:
    print('TypeError')

# Issue #17077: segfault with __new__ returning NULL
class C(_testcapi.WithAcquireRelease):
    def __new__(cls):
        return None

try:
    C()
except TypeError:
    print('TypeError')

# Issue #17077: segfault with __new__ returning NULL
