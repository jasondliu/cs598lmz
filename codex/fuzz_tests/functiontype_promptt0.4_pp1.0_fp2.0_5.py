import types
# Test types.FunctionType
def foo(): pass
assert type(foo) == types.FunctionType
assert type(foo) == types.FunctionType

# Test types.ClassType
class foo: pass
assert type(foo) == types.ClassType
assert type(foo) == types.ClassType

# Test types.TypeType
assert type(types) == types.TypeType
assert type(types) == types.TypeType

# Test types.InstanceType
assert type(foo()) == types.InstanceType
assert type(foo()) == types.InstanceType

# Test types.StringType
assert type("") == types.StringType
assert type("") == types.StringType

# Test types.UnicodeType
assert type(u"") == types.UnicodeType
assert type(u"") == types.UnicodeType

# Test types.IntType
assert type(1) == types.IntType
assert type(1) == types.IntType

# Test types.LongType
assert type(1L) == types.LongType
assert type(1L) == types.LongType

# Test types
