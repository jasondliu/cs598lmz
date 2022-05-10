import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass
def i(): pass
def j(): pass

print type(f) is types.FunctionType
print type(g) is types.FunctionType
print type(h) is types.FunctionType
print type(i) is types.FunctionType
print type(j) is types.FunctionType

# Test types.BuiltinFunctionType
print type(f) is types.BuiltinFunctionType
print type(g) is types.BuiltinFunctionType
print type(h) is types.BuiltinFunctionType
print type(i) is types.BuiltinFunctionType
print type(j) is types.BuiltinFunctionType

# Test types.MethodType
class A:
    def m(self): pass

print type(A.m) is types.MethodType
print type(A().m) is types.MethodType

# Test types.UnboundMethodType
class B:
    def m(self): pass

print type(B.m) is types.UnboundMethodType

# Test types.LambdaType
l1 =
