import types
# Test types.FunctionType
def foo():
    pass

print(type(foo) == types.FunctionType)

class A:
    def foo(self):
        pass

print(type(A.foo) == types.FunctionType)

# Test types.LambdaType
print(type(lambda: None) == types.LambdaType)

# Test types.GeneratorType
def foo():
    yield 1

print(type(foo()) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
print(type(A.foo) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.foo) == types.UnboundMethodType)

# Test types.ModuleType
print(type(types) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:

