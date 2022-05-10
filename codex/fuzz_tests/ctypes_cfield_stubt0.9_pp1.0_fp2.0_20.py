import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.c_double):
    def __add__(self, other):
        return D(self.value + other.value)

# Test objects with a from_parameter() class method that
# returns a different type:
class S1(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float)]
class B1:
    @classmethod
    def from_param(cls, obj):
        return int(obj.x)
ctypes.B1 = B1

# In some cases a structure contains another as a field.
# There are three possibilities for what to do:
#  1. return a pointer to the structure, because the field
#     is a pointer to the structure,
#  2. return the sub-strucure, because the field is a
#     structure by value, or
#  3. return an object which has the same fields as the
#     field sub-structure, and which delegates to it.

# 1.
class S2(ctypes.Structure):
    _fields_ = [
