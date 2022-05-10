import ctypes
# Test ctypes.CField
import ctypes
class X(ctypes.Structure):
    _fields_ = [('p', ctypes.c_int * 4), ('s', ctypes.c_char * 8)]

x = X(i for i in range(4))
for i in x.p:
    print(i)
x.s = b"abc123\0"
print(x.s)
"""

"""
# Test 'lazy' properties
class C(object):
    exec('def getx(self): return 42')
    x = property(getx)

c = C()
print('expect 42', c.x)
"""

"""
# Bug. The optimizer transformed this into list.__index__,
# which is not supported. A list is always 0 in Python 2.
c = ([0,1],list)
c[1].index(1,1,2)
"""

"""
# Bug. tuple.__index__ returned an incorrect value.
class C(object):
    def __index__(self):
        return 42

print([0,C(),
