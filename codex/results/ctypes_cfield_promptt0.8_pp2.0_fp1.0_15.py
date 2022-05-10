import ctypes
# Test ctypes.CField
try:
    ctypes.CField()
except TypeError:
    pass
else:
    print('Test failed')

try:
    ctypes.CField('', 42, '')
except TypeError:
    pass
else:
    print('Test failed')

try:
    ctypes.CField('', (), '')
except TypeError:
    pass
else:
    print('Test failed')

try:
    ctypes.CField('', (1,), '')
except TypeError:
    pass
else:
    print('Test failed')

ctypes.CField('', (1, 2), '')
# Test ctypes.Structure

try:
    class Bad1(ctypes.Structure):
        _fields_ = 42
except TypeError:
    pass
else:
    print('Test failed')

try:
    class Bad2(ctypes.Structure):
        _fields_ = [1, 2, 3]
except TypeError:
    pass
else:
    print('Test failed')

try:
    class Bad3
