import types
# Test types.FunctionType
def func(): pass
print(type(func) == types.FunctionType)

# Test types.LambdaType
x = lambda: None
print(type(x) == types.LambdaType)

# Test types.GeneratorType
def gen(): yield 1
g = gen()
print(type(g) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class C:
    def meth(self): pass
c = C()
print(type(c.meth) == types.MethodType)

# Test types.UnboundMethodType
print(type(C.meth) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    tb = sys.
