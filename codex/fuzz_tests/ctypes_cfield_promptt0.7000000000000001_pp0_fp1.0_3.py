import ctypes
# Test ctypes.CField
import datetime

def test_CField():
    assert datetime.MINYEAR == 1

# Test ctypes.Structure
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

def test_Structure():
    pt = POINT(15, 25)
    assert pt.x == 15
    assert pt.y == 25
    pt.x = 10
    pt.y = 20
    assert pt.x == 10
    assert pt.y == 20

# Test ctypes.Union
class MyUnion(ctypes.Union):
    _fields_ = [('longval', ctypes.c_long),
                ('doubleval', ctypes.c_double)]

def test_Union():
    mu = MyUnion(longval = 3)
    assert mu.doubleval == 3.0
    mu.doubleval = 3.3
    assert mu.longval == 3

# Test ctypes._Pointer
class my_struct(ctypes.Structure
