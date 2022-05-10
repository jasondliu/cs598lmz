import ctypes
# Test ctypes.CField
def cf(obj):
    print(
    '  Name:', obj.__name__,
    'Offset:', obj.offset,
    'Type:', obj.ctype,
    'Size:', obj.size,
    'Align:', obj.alignment,
    'Bits:', obj.bits,
    'Flags:', obj.flags,
    sep='\n', end='\n\n')

cf(ctypes.CField(ctypes.c_int))
cf(ctypes.CField('i', ctypes.c_int, 0))
cf(ctypes.CField('i', ctypes.c_int, 0, 10))
cf(ctypes.CField('i', ctypes.c_int, 0, 10, 1))
cf(ctypes.CField('i', ctypes.c_int, 0, 10, 1, ctypes.CFUNCTYPE(ctypes.c_int)))
cf(ctypes.CField('i', ctypes.c_int, 0, 10, 1, ctypes.CFUNCTYPE
