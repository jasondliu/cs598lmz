import types
# Test types.FunctionType
import types

def f():
    pass

print isinstance(f, types.FunctionType)

# Test types.GeneratorType
def f():
    yield 1

print isinstance(f(), types.GeneratorType)

# Test types.LambdaType
print isinstance((lambda x: x), types.LambdaType)

# Test types.ListType
print isinstance([], types.ListType)

# Test types.ModuleType
import sys
print isinstance(sys, types.ModuleType)

# Test types.TypeType
import types
print isinstance(types, types.TypeType)

# Test types.UnboundMethodType
import types
class C(object):
    def f(self): pass
print isinstance(C.f, types.UnboundMethodType)

# Test types.BuiltinFunctionType
import types
print isinstance(abs, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
import types
print isinstance([].append, types.BuiltinMethodType)

# Test types.ClassType
import
