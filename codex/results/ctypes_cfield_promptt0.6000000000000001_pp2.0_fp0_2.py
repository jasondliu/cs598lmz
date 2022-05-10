import ctypes
# Test ctypes.CField
class FIELD_TYPE(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

class FIELD_NAME_TYPE(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    _name_ = "foo"

class FIELD_TYPE_NAME(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    _type_ = "foo"

class FIELD_NAME_TYPE_NAME(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    _name_ = "foo"
    _type_ = "foo"

class FIELD_NAME_TYPE_NAMES(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]
    _name_ = "foo"
    _type_ = "foo"
    _names_ = ["foo"]

class FIELD_NAME_TYPE_NAMES_NO_NAME(ctypes.Structure):
    _
