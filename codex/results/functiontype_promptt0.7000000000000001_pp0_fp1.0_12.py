import types
# Test types.FunctionType
def f(): pass
def g(): pass
print(type(f) is types.FunctionType)
print(type(g) is types.FunctionType)
print(type(lambda x: x) is types.FunctionType)
print(type(f) is types.LambdaType)
print(type(g) is types.LambdaType)
print(type(lambda x: x) is types.LambdaType)

# Test types.ClassType
class A: pass
class B(object): pass
print(type(A) is types.ClassType)
print(type(B) is types.ClassType)

# Test types.InstanceType
print(type(A()) is types.InstanceType)
print(type(B()) is types.InstanceType)

# Test types.MethodType
class C:
    def m(self):
        pass
print(type(C.m) is types.MethodType)
print(type(C().m) is types.MethodType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunction
