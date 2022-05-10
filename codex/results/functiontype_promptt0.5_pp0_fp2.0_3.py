import types
# Test types.FunctionType
def f():
    pass

print type(f) == types.FunctionType

# Test types.MethodType
class A:
    def f(self):
        pass

print type(A.f) == types.MethodType

# Test types.BuiltinFunctionType
print type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
print type([].append) == types.BuiltinMethodType

# Test types.ModuleType
import types
print type(types) == types.ModuleType

# Test types.ClassType
print type(A) == types.ClassType

# Test types.TypeType
print type(type) == types.TypeType

# Test types.InstanceType
print type(A()) == types.InstanceType

# Test types.UnboundMethodType
print type(A.f) == types.UnboundMethodType
