import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun called")
    return "fun return"

class TestClass(object):
    def fun(self):
        print("class fun called")
    def __init__(self):
        self.fun_1 = fun

a = TestClass()
print(a.fun_1())
