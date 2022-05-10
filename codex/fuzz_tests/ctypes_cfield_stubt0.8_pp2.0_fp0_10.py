import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

fields = [getattr(S, field) for field in S._fields_]

# <cfield 'x' of 'S' objects>
print(fields)

# <cfield 'x' of 'S' objects>
print(fields[0])

fields[0].__name__ = 'Invalid'
#Traceback (most recent call last):
#  File "ctypes_missing_set_name.py", line 15, in <module>
#    fields[0].__name__ = 'Invalid'
#AttributeError: readonly attribute
