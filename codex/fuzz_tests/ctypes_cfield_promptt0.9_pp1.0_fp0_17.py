import ctypes
# Test ctypes.CField()

libc = ctypes.CDLL(ctypes.util.find_library("c"))

class bar(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

    class u(ctypes.Union):
        _fields_ = [
            ("xxx", ctypes.c_int),
            ("bar", ctypes.CField("yyy", bar)),
        ]

    _anonymous_ = ("u",)

def test_1():
    assert bar._fields_[0][0] == "b"
    assert bar._fields_[0]._name == "b"

    assert bar._anonymous_ == ("u",)
    assert bar.u._fields_[0][0] == "xxx"
    assert bar.u._fields_[1][0] == "bar"
    assert bar.u._fields_[0]._name == "xxx"
    assert bar.u._fields_[1]._name == "bar"

    bar_struct = bar()

    assert bar_struct.bar
    assert bar_struct
