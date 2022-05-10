import ctypes
# Test ctypes.CField

class CTest(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)]

class CTestSub(CTest):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int)]

class CTestSubSub(CTestSub):
    _fields_ = [
        ('c', ctypes.c_int),
        ('d', ctypes.c_int)]

class CTestSubSubSub(CTestSubSub):
    _fields_ = [
        ('e', ctypes.c_int),
        ('f', ctypes.c_int)]

class CTestSubSubSubSub(CTestSubSubSub):
    _fields_ = [
        ('g', ctypes.c_int),
        ('h', ctypes.c_int)]

class CTestSubSubSubSubSub(CTestSubSubSubSub):
    _fields_ = [
        ('i', ctypes.c_int),
