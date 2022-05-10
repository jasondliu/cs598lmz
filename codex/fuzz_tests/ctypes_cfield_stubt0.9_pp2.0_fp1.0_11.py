import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert ctypes.CField.__name__ == "CField"
assert ctypes.CField is ctypes.c_int

ctypes.CFieldType = type(S._fields_[0])
assert ctypes.CFieldType.__name__ == "CFieldType"

ctypes.CFieldPtr = type(S.x)
assert ctypes.CFieldPtr.__name__ == "CFieldPtr"

ctypes.CFieldPtrType = type(S._fields_[0])
assert ctypes.CFieldPtrType.__name__ == "CFieldPtrType"

# For function types, the check is a bit more complicated.
from ctypes import CFUNCTYPE
import os
PAGESIZE = os.sysconf("SC_PAGE_SIZE")

class S1(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_long)]

class S2(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_long)]

S1_S2_S1_P = CF
