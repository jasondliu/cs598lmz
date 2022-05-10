import ctypes
# Test ctypes.CField
class test_field_c(ctypes.Structure):
    pass

class test(ctypes.Structure):
    _fields_ = [("field", test_field_c)]

test._fields_[0]._type_.type
test._fields_[0]._type_.name
test._fields_[0]._type_.align
test._fields_[0]._type_.ref
test._fields_[0]._type_.len
test._fields_[0]._type_.shape
test._fields_[0]._type_.flags
test._fields_[0]._type_.cname
test._fields_[0]._type_.name
test._fields_[0]._type_.strides
test._fields_[0]._type_.subdtype
test._fields_[0]._type_.subarray
test._fields_[0]._type_.suboffset
test._fields_[0]._type_.argtypes
test._fields_[0]._type_.restype
test._fields_[0]._type_.errestype
test._fields_[0]._
