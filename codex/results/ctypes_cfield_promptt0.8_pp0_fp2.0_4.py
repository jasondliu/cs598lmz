import ctypes
# Test ctypes.CField
class TestCF:
    def __init__(self, value):
        self.value = value
class TestCFs(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.CField(TestCF)),
    ]
# Test ctypes.Array:
class TestArray:
    def __init__(self, value):
        self.value = value
class TestArrays(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.Array(TestArray, 9)),
    ]
# Test ctypes.Bool:
class TestBools(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.Array(ctypes.Bool, 9)),
    ]
# Test ctypes.PYFUNCTYPE:
CPY_CALLBACK_FUNC_PTR = ctypes.PYFUNCTYPE(None)
class TestCbFuncPtrs(ctypes.Structure):
    _fields_ = [
        ('value', CPY_CALLBACK_FUNC_PTR),
