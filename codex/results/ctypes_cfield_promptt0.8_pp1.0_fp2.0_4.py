import ctypes
# Test ctypes.CField.
import tests.wrap

# The ctypes object that has been auto-created by TestObj has a
# ctypes.CField member, containing the appropriate type information.
TestObj = tests.wrap.TestObj

assert TestObj._fields_ == [('value', ctypes.c_int)]
assert TestObj.value._type_ == ctypes.c_int
