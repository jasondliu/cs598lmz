import types
# Test types.FunctionType, types.LambdaType, types.ClassType and
# types.InstanceType:
print types.FunctionType
print types.LambdaType
print types.ClassType
print types.InstanceType
print types.TypeType

def g(): pass
def f(x = g): pass
print type(g)
print type(f.func_defaults[0])
print type(types)
class C: pass
print type(C)
print type(C())
print type(type)

# Test __bases__
print types.FunctionType.__bases__
print types.LambdaType.__bases__
print types.ClassType.__bases__
print types.InstanceType.__bases__
print types.TypeType.__bases__
print int.__bases__
print type(types.FunctionType.__bases__[0]).__name__

# Test the ModuleType type
import types
print type(types).__name__

# Test if using built-in function types outside of the types module fails
try:
    print FunctionType(None,
