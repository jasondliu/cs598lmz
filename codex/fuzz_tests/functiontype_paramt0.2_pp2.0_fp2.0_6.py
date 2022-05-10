from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the __code__ attribute of a function is a code object.
def f(): pass
import types
isinstance(f.__code__, types.CodeType)

# Test that the __code__ attribute of a method is a code object.
class C:
    def m(self): pass
isinstance(C.m.__code__, types.CodeType)

# Test that the __code__ attribute of a builtin is a code object.
import builtins
isinstance(builtins.len.__code__, types.CodeType)

# Test that the __code__ attribute of a class is a code object.
class C: pass
isinstance(C.__code__, types.CodeType)

# Test that the __code__ attribute of a class method is a code object.
class C:
    @classmethod
    def m(cls): pass
isinstance(C.m.__code__, types.CodeType)

# Test that the __code__ attribute of a static method is a code object.
class C:
