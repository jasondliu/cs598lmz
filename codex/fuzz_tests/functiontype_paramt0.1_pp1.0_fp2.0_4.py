from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the __code__ attribute of a function is a code object.
def f(): pass
assert isinstance(f.__code__, types.CodeType)

# Test that the __code__ attribute of a method is a code object.
class C:
    def f(self): pass
assert isinstance(C.f.__code__, types.CodeType)

# Test that the __code__ attribute of a builtin function is a code object.
assert isinstance(len.__code__, types.CodeType)

# Test that the __code__ attribute of a builtin method is a code object.
assert isinstance(list.append.__code__, types.CodeType)

# Test that the __code__ attribute of a method descriptor is a code object.
assert isinstance(list.__dict__['append'].__code__, types.CodeType)

# Test that the __code__ attribute of a wrapper descriptor is a code object.
assert isinstance(list.__dict__['__len__'].__code__, types.
