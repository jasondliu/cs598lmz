import ctypes
# Test ctypes.CField

# The following structure is defined in the C header file:
#
#   struct S {
#       int a;
#       int b;
#       int c;
#   };
#
# The following Python code defines a ctypes structure class
# corresponding to this C structure.

class S(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]

# This CField instance represents the field 'a' of structure S.
f = S.a

# This is the offset of field 'a' in the structure.
print('offset of field a:', f.offset)

# This is the offset of field 'b' in the structure.
print('offset of field b:', S.b.offset)

# This is the offset of field 'c' in the structure.
print('offset of field c:', S.c.offset)

# This is the size of field 'a' in the structure.
print('
