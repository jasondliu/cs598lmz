import types
# Test types.FunctionType
def func(): pass
print(type(func) is types.FunctionType)
# True

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
# True

# Test types.LambdaType
print(type(lambda x: x) is types.LambdaType)
# True

# Test types.GeneratorType
def gen():
    yield 1
print(type(gen()) is types.GeneratorType)
# True

# Test types.MethodType
class A:
    def method(self): pass
print(type(A.method) is types.MethodType)
# True

# Test types.UnboundMethodType
print(type(A.method) is types.UnboundMethodType)
# True

# Test types.BuiltinMethodType
print(type(str.replace) is types.BuiltinMethodType)
# True

# Test types.ModuleType
print(type(types) is types.ModuleType)
# True

# Test types.TracebackType
try:
    raise Exception()

