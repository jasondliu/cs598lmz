import types
# Test types.FunctionType

def f():
    pass

def g():
    pass

print(type(f) is types.FunctionType)
print(type(g) is types.FunctionType)

class C:
    def m(self):
        pass

print(type(C.m) is types.FunctionType)
print(type(C.m) is types.UnboundMethodType)

class D:
    def __init__(self):
        self.m = lambda: None

d = D()
print(type(d.m) is types.FunctionType)
print(type(d.m) is types.MethodType)
