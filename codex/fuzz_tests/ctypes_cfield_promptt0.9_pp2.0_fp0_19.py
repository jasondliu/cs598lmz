import ctypes
# Test ctypes.CField.
import _ctypes_test
import ctypes.wintypes


class MyModel(ctypes.Structure):
    _fields_ = [
        ("_packed", ctypes.c_byte, 1),
        ("counter", ctypes.c_byte, 7)]


m1 = MyModel(1, 11)
assert m1.counter == 3
m2 = MyModel(2, 12)
assert m2.counter == 4
foo = _ctypes_test.MyModel()
assert foo.counter == 5
foo.counter = 6
assert foo.counter == 6
