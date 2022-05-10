import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self, *args):
        self._as_parameter_ = ctypes.c_int()

    def _check_retval_(self):
        return 1

c = C()

print(type(c))
print(type(c._as_parameter_))

print(type(S.x))
print(type(c._as_parameter_) is ctypes.CField)

c._as_parameter_ = 1
print(c._as_parameter_)
z = c._as_parameter_
c._as_parameter_ = z
c._as_parameter_ += 3

# This will fail with:
# TypeError: 'CField' object does not support item assignment
# c._as_parameter_[0] = 1

s = S()
s.x = c._as_parameter_

# This will fail with:
# TypeError: 'CField' object does not support item assignment
# s.x = c._as_parameter_[0]

try
