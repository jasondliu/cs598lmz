import types
# Test types.FunctionType
def f(x):
    return x

print(type(f) is types.FunctionType)

# Test types.LambdaType
print(type(lambda x: x) is types.LambdaType)

# Test types.GeneratorType
print(type((x for x in range(10))) is types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)

# Test types.MethodType
class C:
    def method(self): pass
print(type(C.method) is types.MethodType)

# Test types.UnboundMethodType
print(type(C.method) is types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    exc_info = sys.exc_info()
print
