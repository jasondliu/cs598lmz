import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.ClassType
class C:
    pass

assert type(C) is types.ClassType

# Test types.UnboundMethodType
assert type(C.__init__) is types.UnboundMethodType

# Test types.MethodType
c = C()
assert type(c.__init__) is types.MethodType

# Test types.InstanceType
assert type(c) is types.InstanceType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.GeneratorType
def g():
    yield 1

assert type(g()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception()
except:
    assert type(sys.exc_info()[2]) is types
