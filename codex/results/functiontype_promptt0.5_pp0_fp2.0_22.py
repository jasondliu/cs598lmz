import types
# Test types.FunctionType
def func(a):
    return a
print isinstance(func, types.FunctionType)

# Test types.GeneratorType
def generator():
    yield 1
print isinstance(generator, types.GeneratorType)

# Test types.LambdaType
lam = lambda x: x * x
print isinstance(lam, types.LambdaType)

# Test types.CodeType
print isinstance(func.func_code, types.CodeType)

# Test types.TypeType
print isinstance(str, types.TypeType)

# Test types.BuiltinFunctionType
print isinstance(str, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print isinstance('', types.BuiltinMethodType)

# Test types.ModuleType
print isinstance(types, types.ModuleType)

# Test types.UnboundMethodType
class A(object):
    def foo(self):
        pass
print isinstance(A.foo, types.UnboundMethodType)

# Test types.InstanceType
class B(object):
   
