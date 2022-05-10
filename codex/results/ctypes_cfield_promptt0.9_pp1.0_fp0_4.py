import ctypes
# Test ctypes.CField (not CFields from hereon)

class CFoo(ctypes.LittleEndianStructure):
    _fields_ = [('first', ctypes.c_int),
                ('second', ctypes.c_char),
                ('third', ctypes.c_int),
                ]

class CBar(ctypes.Structure):
    first = ctypes.CField(ctypes.c_char)
    second = ctypes.CField(ctypes.c_int, offset=8)

print CFoo
print CFoo().first
print CFoo().second
print CFoo().third
try:
    CFoo().first.value = "foo"
    print "Unexpected"
except ValueError:
    pass

print CBar
try:
    CBar().first = "a"
    print "Unexpected"
except TypeError:
    print CBar().first

CBa
