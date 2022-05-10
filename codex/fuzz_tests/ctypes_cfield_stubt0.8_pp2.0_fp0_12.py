import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

assert C._fields_[0][1] == ctypes.CField
s = S()
c = C(s)
print c.x
print c.x.__class__

# verify that ctypes.CField is removed
assert not hasattr(ctypes, 'CField')

try:
    ctypes.CField
    assert 0
except AttributeError:
    pass

try:
    C._fields_[0][1] = ctypes.CField
    assert 0
except AttributeError:
    pass
</code>
Python 3 code
The same as above but with some minor changes to work with Python 3.
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

import ctypes._ctypes_test
ctypes._ctypes_test.CField = type(S.x)

class C(ctypes.Structure):
    _
