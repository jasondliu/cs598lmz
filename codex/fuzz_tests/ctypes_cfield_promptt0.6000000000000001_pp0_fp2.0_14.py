import ctypes
# Test ctypes.CField: simple field type
class TestCF(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

class TestCF2(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3)]

class TestCF3(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3 * 2)]

class TestCF4(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3 * 2 * 4)]

class TestCF5(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3 * 2 * 4 * 5)]

class TestCF6(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3 * 2 * 4 * 5 * 6)]

class TestCF7(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3 * 2 * 4 * 5 * 6 * 7)]

def test_cfield():

