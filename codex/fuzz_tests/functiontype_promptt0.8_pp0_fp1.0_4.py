import types
# Test types.FunctionType.
def f(): pass

assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert isinstance(s2, types.FunctionType)

# Test the type of a basic function.
assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(s2) is types.FunctionType

class C:
    # Test the type of a method.
    def method(self): pass

    assert isinstance(method, types.FunctionType)
    assert isinstance(C.method, types.FunctionType)
    assert type(method) is types.FunctionType
    assert type(C.method) is types.FunctionType

# Test the type of a class.
class C: pass

assert isinstance(C, types.ClassType)  # Python 2 only
assert type(C) is types.ClassType  # Python 2 only

# Test the type of a static method.
class C:
    @staticmethod
    def static_method(): pass

assert isinstance(C.static_method,
