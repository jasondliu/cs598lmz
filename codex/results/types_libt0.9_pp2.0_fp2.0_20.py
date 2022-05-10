import types
types.MethodType(lambda self, x: 1, None)

try:
    types.MethodType
except NameError:
    import struct
