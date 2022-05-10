import types
# Test types.FunctionType
def fn(x):
    return x
print(type(fn) == types.FunctionType)
# Test types.ClassType
class C:
    pass
print(type(C) == types.ClassType)
# Test types.UnboundMethodType
print(type(C.__init__) == types.UnboundMethodType)
# Test types.InstanceType
c = C()
print(type(c) == types.InstanceType)
# Test types.MethodType
print(type(c.__init__) == types.MethodType)
# Test types.BuiltinFunctionType
print(type(chr) == types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)
# Test types.ModuleType
import types
print(type(types) == types.ModuleType)
# Test types.TypeType
print(type(type) == types.TypeType)
# Test types.SliceType
print(type(slice(1)) == types.SliceType)
# Test types.TracebackType
try
