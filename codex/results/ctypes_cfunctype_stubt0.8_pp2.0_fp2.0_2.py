import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())

class C(object):
    def __init__(self):
        self.val = 42
        self.doit = FUNTYPE(self.doit)
    def doit(self):
        return self.val
print(C().doit())

class C(object):
    def __init__(self):
        self.val = 42
        # self.go() is called
        self.doit = FUNTYPE(self.go)
    def go(self):
        return self.val
print(C().doit())
</code>

