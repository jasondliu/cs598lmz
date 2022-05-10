import types
# Test types.FunctionType
def f():
    pass
print(type(f) is types.FunctionType)
print(type(lambda: None) is types.LambdaType)
print(type((x for x in range(10))) is types.GeneratorType)

# Test types.MethodType
class C:
    def method(self):
        pass
print(type(C.method) is types.MethodType)
c = C()
print(type(c.method) is types.MethodType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
print(type(iter) is types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)
print(type({}.get) is types.BuiltinMethodType)

# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    exc_type, exc_value, exc_tb
