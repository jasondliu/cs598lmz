import types
# Test types.FunctionType
class A:
    def f(self): pass

def g(): pass

print type(A.f) is types.MethodType
print type(g) is types.FunctionType

# Test types.UnboundMethodType
print type(A.f) is types.UnboundMethodType
# Test types.MethodType
print type(A().f) is types.MethodType

print type(len) is types.BuiltinFunctionType
print type(len) is types.BuiltinMethodType

class C:
    def __len__(self): return 0

print type(C().__len__) is types.MethodType

class D(object):
    def __len__(self): return 0

print type(D().__len__) is types.MethodType
