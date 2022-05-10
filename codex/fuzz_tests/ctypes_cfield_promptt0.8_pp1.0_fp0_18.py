import ctypes
# Test ctypes.CField
print('--- Test CField ---')
class TestCF(ctypes.Structure):
    _fields_ = [
        ("first", ctypes.CField),
        ("second", ctypes.CField),
    ]

class Test(ctypes.Structure):
    _fields_ = [
        ("field", ctypes.c_int),
        ("next", ctypes.POINTER(Test)),
    ]
    _anonymous_ = ("first", "second")

test = TestCF.in_dll(ctypes.CDLL('./libtest.so'), 'test')
test2 = Test()
test2.next = ctypes.pointer(test2)
test.second.next = ctypes.pointer(test2)
# Test ctypes.Array
print('--- Test Array ---')
class Test(ctypes.Structure):
    _fields_ = [
        ("field", ctypes.c_int),
        ("array", ctypes.c_int * 5),
        ("array_char", ctypes.c_char * 5),
    ]

test = Test.
