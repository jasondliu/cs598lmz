from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the __code__ attribute of a function is a code object
def f(): pass
assert type(f.__code__) is type(f.__code__)

# Test that the __code__ attribute of a builtin function is None
assert type(len.__code__) is type(None)

# Test that the __code__ attribute of a method is a code object
class C:
    def m(self): pass
assert type(C.m.__code__) is type(C.m.__code__)

# Test that the __code__ attribute of a builtin method is None
assert type(C.__str__.__code__) is type(None)

# Test that the __code__ attribute of a method descriptor is None
assert type(list.append.__code__) is type(None)

# Test that the __code__ attribute of a class is None
assert type(C.__code__) is type(None)

# Test that the __code__ attribute of a module is None
import sys
assert
