import types
# Test types.FunctionType and types.MethodType in the same way
types_to_test = [types.FunctionType, types.MethodType]
for type in types_to_test:
    if type is not None and hasattr(type, "__code__"):
        try:
            type.__code__ = lambda self: None
            raise TestFailed, "should not be able to assign to __code__"
        except TypeError:
            pass

# test that the magic __code__ attribute of functions and methods
# always returns a code object
def f(x): return x
types_to_test = [type(f), types.FunctionType, types.MethodType]
for type in types_to_test:
    if type is not None and hasattr(type, "__code__"):
        try:
            temp = type.__code__
            if not isinstance(temp, types.CodeType):
                raise TestFailed, "__code__ should return a code object"
        except TypeError:
            pass

# test that the magic __globals__ attribute of functions and methods
# always returns
