import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType), "f should be a function"
assert type(f) is types.FunctionType, "f should be a function"
assert f.__class__ is types.FunctionType, "f should be a function"

print "OK"
