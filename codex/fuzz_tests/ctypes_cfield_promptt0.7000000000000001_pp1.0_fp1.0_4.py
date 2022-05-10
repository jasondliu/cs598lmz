import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

class RECT(ctypes.Structure):
    _fields_ = [
        ('left', ctypes.c_int),
        ('top', ctypes.c_int),
        ('right', ctypes.c_int),
        ('bottom', ctypes.c_int),
    ]

def exampleTest():
    # This function takes no arguments and returns no arguments
    print("call exampleTest")
    dll = ctypes.CDLL("dllTest.dll")
    myDllFuncTest = dll.exampleTest
    myDllFuncTest()

def exampleTest1(a, b):
    # This function takes no arguments and returns no arguments
    print("call exampleTest1")
    dll = ctypes.CDLL("dllTest.dll")
    myDllFuncTest1 = dll.exampleTest1
    myDllFuncTest1.argtype
