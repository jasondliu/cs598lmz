import types
# Test types.FunctionType
def func(): pass
print(type(func) is types.FunctionType)
print(isinstance(func, types.FunctionType))

# Test types.LambdaType
lam = lambda: None
print(type(lam) is types.LambdaType)
print(isinstance(lam, types.LambdaType))

# Test types.GeneratorType
gen = (i for i in range(3))
print(type(gen) is types.GeneratorType)
print(isinstance(gen, types.GeneratorType))

# Test types.CodeType
print(type(func.__code__) is types.CodeType)
print(isinstance(func.__code__, types.CodeType))

# Test types.MethodType
class Class:
    def method(self):
        pass
print(type(Class.method) is types.MethodType)
print(isinstance(Class.method, types.MethodType))

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
print(isinstance(len, types.
