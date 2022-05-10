import types
# Test types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
import builtins
assert isinstance(id, types.BuiltinFunctionType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.BooleanType
assert isinstance(True, types.BooleanType)
assert isinstance(False, types.BooleanType)

# Test types.NoneType
assert isinstance(None, types.NoneType)

# Test types.StringTypes
assert isinstance("abc", types.StringTypes)
assert isinstance(u"abc", types.StringTypes)

# Test types.BufferType
import array
a = array.array('c', "abc")
assert isinstance(a, types.BufferType)

# Test types.ObjectType
#assert isinstance(types.ObjectType, types.ObjectType)

# Test types.TracebackType
def g():
    1/0
try:
    g()
except:
    import sys
    tb = sys.exc_info()[2]
