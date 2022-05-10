import ctypes
# Test ctypes.CField (created for issue #7427)
class RenamedField(ctypes.Structure):
    _fields_ = [('my_field', ctypes.c_int)]
    _anonymous_ = RenamedField._fields_[0]

class NonAnonymous(ctypes.Structure):
    _fields_ = RenamedField._anonymous_

class Anonymous(ctypes.Structure):
    _fields_ = RenamedField._anonymous_
    _anonymous_ = Anonymous._fields_[0]

class BadType(ctypes.Structure):
    _fields_ = [('my_field', ctypes.c_int)]
    _anonymous_ = BadType._fields_

class NoFields(ctypes.Structure):
    _anonymous_ = ('a', 'b', 'c')

class NotTuple(ctypes.Structure):
    _anonymous_ = 'abc'

class InvalidLength(ctypes.Structure):
    _fields_ = [('f1', ctypes.c_int)]
    _anonymous_ = ('a', 'b',
