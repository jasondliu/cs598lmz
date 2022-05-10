import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__doc__ = "field of C structure"

class C(ctypes.Structure):
    _fields_ = [('y', S)]

print(C.y.x)
print(C.y.x.__class__)
print(int(C.y.x))

# CPython issue #31368: We now have a cyclic reference between the
# docs of the CField and the StructureField. 'y.x' (CField) has a
# ref to the StructureField 'y', while 'y' (StructureField) has a
# ref to the CField 'x'. The docs were then leaking, because
# cyclic-gc can't free them.

# Before the fix, we would get e.g.:
#
#  Fatal Python error: GC object already tracked
#
# when running this test.
