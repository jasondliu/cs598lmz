import ctypes
# Test ctypes.CField
class c_zval(ctypes.Structure):
    _fields_ = [('value', ctypes.CField)]

# Check it's the same as the fields specified by
# the trivial _pack_ attribute
class pack_zval(ctypes.Structure):
    _fields_ = [('value', ctypes.CField)]
    _pack_ = 1

print c_zval._pack_
print c_zval._fields_[0][1]

# This is a ValueError.  We specified _pack_, so
# we cannot specify the alignment field.
import test.test_support
test.test_support.check_py3k_warnings()

class c_zval2(ctypes.Structure):
    _fields_ = [('value', ctypes.CField)]
    _pack_ = 1
    _align_ = "field"

print c_zval2._pack_
print c_zval2._fields_[0][1]
