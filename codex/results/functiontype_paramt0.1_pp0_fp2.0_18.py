from types import FunctionType
list(FunctionType(lambda: None, globals()))

# Test that the __code__ attribute of a function is a code object.
def f(): pass
assert isinstance(f.__code__, types.CodeType)

# Test that the __code__ attribute of a method is a code object.
class C:
    def m(self): pass
assert isinstance(C.m.__code__, types.CodeType)

# Test that the __code__ attribute of a built-in function is a code object.
assert isinstance(len.__code__, types.CodeType)

# Test that the __code__ attribute of a built-in method is a code object.
assert isinstance(list.append.__code__, types.CodeType)

# Test that the __code__ attribute of a method descriptor is a code object.
assert isinstance(list.__dict__['append'].__code__, types.CodeType)

# Test that the __code__ attribute of a class is a code object.
assert isinstance(C.__code__, types.CodeType)

# Test that the __code
