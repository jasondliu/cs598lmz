import ctypes
# Test ctypes.CField.__str__()
# NOTE: This test might crash if Python is built in Debug mode with MSVC.
# See also http://bugs.python.org/issue7991 .
import _ctypes_test
CField = _ctypes_test.CField
__Pyx_CField = CField
try:
    _ctypes_test.fields[0]
except ValueError as e:
    f = CField(0, 0, 0, 0, 0, 0)
    try:
        b = f.__str__()
    except:
        print(e)
    else:
        raise AssertionError
else:
    print('ERROR: CField ctor test failed')
