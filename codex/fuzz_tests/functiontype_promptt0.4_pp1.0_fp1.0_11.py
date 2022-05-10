import types
# Test types.FunctionType
def f():
    pass

print(type(f) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(int) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(str.upper) == types.BuiltinMethodType)
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
def f(self):
    pass
print(type(f) == types.FunctionType)
print(type(f.__get__(int)) == types.MethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except Exception as e:
    print(type(e.__traceback__) == types.
