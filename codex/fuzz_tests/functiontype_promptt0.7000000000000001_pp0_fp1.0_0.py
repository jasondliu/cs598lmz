import types
# Test types.FunctionType
def foo():
	pass

assert  type(foo) == types.FunctionType

# Test types.MethodType
assert type(foo.__call__) == types.MethodType

# Test types.BuiltinFunctionType
assert type(foo.__class__) == types.BuiltinFunctionType

# Test types.TracebackType

# Types are all object types

# Test types.ModuleType
#assert type(types) == types.ModuleType

# Test types.UnboundMethodType
assert type(foo.__call__) == types.MethodType

# Test types.FileType
assert type(sys.stdin) == types.FileType

# Test types.ClassType
assert type(int) == type

# Test types.InstanceType
assert type('foo') == str

# Test types.TypeType
assert type(str) == type

# Test types.XRangeType
assert type(xrange(1,2,3)) == types.XRangeType

# Test types.NoneType
assert type(None) == types.NoneType

# Test types
