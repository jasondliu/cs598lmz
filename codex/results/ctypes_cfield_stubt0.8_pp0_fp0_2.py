import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(type(S.x))

# <class 'CField'>
# A CField object is an instance of this type
# It is used to describe a single field in a C Structure or Union.
#
# This type is a subclass of _CDataDescriptor
# 
#      class CDataDescriptor(_CDataMeta): pass
#
# CDataDescriptor is returned by ctypes.c_int and ctypes.c_char_p.
#
# This type is a subclass of CDataMeta
#
#       class CDataMeta(type): pass
#
# ctypes.c_int is an instance of CDataMeta
# ctypes.c_int.__base__ is CDataMeta
#
# S.x is an instance of CDataDescriptor
# S.x.__base__ is CDataDescriptor
#
# S.x.__base__.__base__ is CDataMeta

# Now let's see what the instance methods are

print(dir(S.x))
print()

# There are only three
#
# __
