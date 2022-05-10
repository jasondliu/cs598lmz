from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test that the repr of a function is evaluable
def f(): pass
repr(f)

# Test that the repr of a method is evaluable
class C:
    def m(self): pass
repr(C.m)

# Test that the repr of a builtin function is evaluable
import sys
repr(sys.exit)

# Test that the repr of a builtin method is evaluable
repr(sys.exit.__call__)

# Test that the repr of a method-wrapper is evaluable
repr(C.m.__get__(C()))

# Test that the repr of a method-wrapper with a custom __repr__ is evaluable
class D:
    def __repr__(self):
        return 'D()'
repr(C.m.__get__(D()))

# Test that the repr of a method-wrapper with a custom __repr__ is evaluable
# even if the custom __repr__ raises an exception
class E:
    def __repr
