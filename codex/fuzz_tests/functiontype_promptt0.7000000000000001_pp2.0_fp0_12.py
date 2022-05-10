import types
# Test types.FunctionType

def f():
    pass

print type(f) == types.FunctionType
print type(lambda: None) == types.FunctionType
print type(f) == types.LambdaType

# Test types.ClassType

class C:
    pass

print type(C) == types.ClassType

D = type('D', (object,), {})
print type(D) == types.ClassType

# Test types.ModuleType

print type(types) == types.ModuleType

# Test types.UnicodeType

print type(u"") == types.UnicodeType

# Test types.BooleanType

print type(True) == types.BooleanType

# Test types.NoneType

print type(None) == types.NoneType

# Test types.LongType

print type(1L) == types.LongType

# Test types.IntType

print type(1) == types.IntType

# Test types.FloatType

print type(1.0) == types.FloatType

# Test types.
