import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class Test(unittest.TestCase):

    def runTest(self):
        # Test from bug #808458
        self.assertEqual(type(S.x), ctypes.CField)

test_support.run_unittest(Test)

# ----------

from ctypes import *

class Test(Structure):
    _fields_ = [("string", c_char * 4)]

obj = Test("asdf")

class Test2(Structure):
    _fields_ = [("string", c_char * 4),
                ("next", POINTER(Test))]

obj2 = Test2("asdf")

class Test3(Structure):
    _fields_ = [("string", c_char * 4),
                ("next", POINTER(Test2))]

obj3 = Test3("asdf")

class Test4(Structure):
    _fields_ = [("string", c_char * 4),
                ("next", POINTER(Test3))]

obj4 = Test4("asdf")

class Test
