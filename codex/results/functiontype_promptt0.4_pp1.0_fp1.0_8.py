import types
# Test types.FunctionType
def f():
    pass
try:
    types.FunctionType(f.func_code, f.func_globals, f.func_name,
                       f.func_defaults, f.func_closure)
except TypeError:
    pass
else:
    print "types.FunctionType() should have raised TypeError"

# Test types.ClassType
class C:
    pass
try:
    types.ClassType('C', (), {})
except TypeError:
    pass
else:
    print "types.ClassType() should have raised TypeError"

# Test types.InstanceType
try:
    types.InstanceType(C)
except TypeError:
    pass
else:
    print "types.InstanceType() should have raised TypeError"

# Test types.MethodType
try:
    types.MethodType(f, C)
except TypeError:
    pass
else:
    print "types.MethodType() should have raised TypeError"

# Test types.UnboundMethodType
try:
    types.UnboundMethodType(f, C)

