import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int*2)]

ctypes.CArrayType = type(S2.x)

class S3(ctypes.Structure):
    pass

_fields_ = []
for name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']:
    _fields_.append((name, ctypes.c_int))
S3._fields_ = _fields_

ctypes.CStructure = type(S3)

################################################################

def eq_(a, b):
    if (a != b):
        print(repr(a), '!=', repr(b))

def contains(container, item):
    for element in container:
        if element == item:
            break
    else:
        print(repr(container), 'does not contain', repr(item))

def P(format, *args):
