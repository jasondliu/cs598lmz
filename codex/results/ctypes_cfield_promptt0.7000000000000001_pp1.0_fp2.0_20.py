import ctypes
# Test ctypes.CField()
try:
    ctypes.CField()
except TypeError:
    pass
else:
    print('ERROR: expected TypeError from ctypes.CField()')

import ctypes.test.test_cfield

print('Test ctypes.CField')
c = ctypes.CField('field', ctypes.c_int, 0)
print(repr(c))
print(c.ofs, c.size)

print('Test struct_1')
print(ctypes.test.test_cfield.struct_1)

print('Test struct_2')
print(ctypes.test.test_cfield.struct_2)
