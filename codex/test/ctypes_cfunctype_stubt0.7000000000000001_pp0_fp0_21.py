import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun")

@FUNTYPE
def fun2():
    print("fun2")

def test():
    print("test")

class Test:
    def __init__(self, x):
        self.x = x
        self.fun = FUNTYPE(self.fun)
    def fun(self):
        print(self.x)

t = Test(4)

t.fun()
fun2()

def fun3():
    print("fun3")

def fun4():
    print("fun4")

def fun5():
    print("fun5")

def fun6():
    print("fun6")

def fun7():
    print("fun7")

def fun8():
    print("fun8")

def fun9():
    print("fun9")

def fun10():
    print("fun10")
