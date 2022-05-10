import ctypes
# Test ctypes.CField
import _ctypes_test
lib = _ctypes_test.dll

class Struct(ctypes.Structure):
    _fields_ = [
        ('foo', ctypes.CField)]

def test_getfield(obj, buf, offset, size, restype):
    def g(obj, buf, offset, size, restype, func):
        return func.__ctypes_from_outparam__(
            ctypes.CField.from_address(offset), obj, buf, restype)

    return (offset, ctypes.string_at(offset, 1), '',  None,
            lambda x: False,
            (obj, buf, offset, size, restype, g),
            0, 1)


def test_getitemfield(obj, buf, offset, size, restype):
    def g(obj, buf, offset, size, restype, func):
        return func.__ctypes_from_outparam__(
            ctypes.CField.from_address(offset), obj, buf, restype)

    return (offset, b'\x01',
