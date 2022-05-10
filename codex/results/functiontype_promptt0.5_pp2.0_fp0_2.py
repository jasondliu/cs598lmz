import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C().f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
class C:
    pass
assert isinstance(C.__str__, types.BuiltinMethodType)

# Test types.GeneratorType
def f():
    yield 1
assert isinstance(f(), types.GeneratorType)

# Test types.UnboundMethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.UnboundMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TypeType
assert isinstance(C, types.TypeType)
assert isinstance(int, types.TypeType)
assert isinstance(type, types.TypeType)

# Test
