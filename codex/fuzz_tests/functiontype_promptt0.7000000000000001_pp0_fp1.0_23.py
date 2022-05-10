import types
# Test types.FunctionType : bug #633286.
def f(): pass
def check(obj, name):
    if type(obj) is not types.FunctionType:
        raise AssertionError("%s:%r is not a function"%(name, obj))
check(f, "f")
check(check, "check")
check(types.FunctionType, "types.FunctionType")
