import ctypes
# Test ctypes.CField.from_address.
#
# This is deliberately hand coded.  Please use the docs to update it.
#
# In this test, the fields are:
#    int   i
#    int  *pi
#    char  c
#    char *pc
#
ctypes.CField.from_address.__doc__ % ctypes.CField._fields_ = (
    ctypes._Field('i', ctypes.c_int),
    ctypes._Field('pi', ctypes.POINTER(ctypes.c_int)),
    ctypes._Field('c', ctypes.c_char),
    ctypes._Field('pc', ctypes.POINTER(ctypes.c_char)),
)

# TODO: test explicit_name
# TODO: test readonly


class MyStruct(ctypes.Structure):
    __slots__ = ('i', 'pi', 'c', 'pc')


class MySubclass(MyStruct):
    __slots__ = ('d', )


# TODO: add test for from_parameter.  from_parameter should
