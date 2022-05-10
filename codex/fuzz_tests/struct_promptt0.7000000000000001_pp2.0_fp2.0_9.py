import _struct
# Test _struct.Struct.__reduce__

from _testcapi import INT_MAX

s = _struct.Struct("i")

for fmt, args in [
    ("i", (4,)),
    ("H", (6,)),
    ("L", (INT_MAX,)),
    ("I", (INT_MAX,)),
    ("Q", (INT_MAX,))]:
    ss = _struct.Struct(fmt)
    s.__reduce__() == (s.__class__, (fmt,))
    s.__reduce__() == ss.__reduce__()
    s.__reduce_ex__(1) == ss.__reduce_ex__(1)
    s.__reduce_ex__(2) == ss.__reduce_ex__(2)
    s.__reduce_ex__(3) == ss.__reduce_ex__(3)
