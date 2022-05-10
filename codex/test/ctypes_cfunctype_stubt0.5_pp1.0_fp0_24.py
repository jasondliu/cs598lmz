import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class X(object):
    def __init__(self):
        self.value = 42
    def getvalue(self):
        return self.value
    def setvalue(self, value):
        self.value = value
    def delvalue(self):
        del self.value
    def fun(self):
        return "hello"
    def fun2(self, x):
        return x

class Y(object):
    def __init__(self):
        self.value = 42
    def getvalue(self):
        return self.value
    def setvalue(self, value):
        self.value = value
    def delvalue(self):
        del self.value
    def fun(self):
        return "hello"
    def fun2(self, x):
        return x

class Z(object):
    def __init__(self):
        self.value = 42
    def getvalue(self):
        return self.value
    def setvalue(self, value):
        self.value = value
