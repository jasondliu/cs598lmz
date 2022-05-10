import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

a = ctypes.c_int(1)
a.value = 2
assert a.value == 2

try:
    a.value = 'spam'
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = a
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S()
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S.x
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S._fields_
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S._fields_[0]
except TypeError:
    pass
else:
    raise AssertionError

try:
    a.value = S
