from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that the repr of a function is evaluable
def f(): pass
repr(f)

# Test that the repr of a method is evaluable
class C:
    def m(self): pass
repr(C.m)

# Test that the repr of a builtin function is evaluable
repr(len)

# Test that the repr of a builtin method is evaluable
repr(list.append)

# Test that the repr of a method descriptor is evaluable
repr(list.__add__)

# Test that the repr of a member descriptor is evaluable
repr(list.__dict__['append'])

# Test that the repr of a wrapper descriptor is evaluable
repr(list.__dict__['__add__'])

# Test that the repr of a class method is evaluable
class C:
    @classmethod
    def cm(cls): pass
repr(C.cm)

# Test that the repr of a static method is evaluable
class C:
    @staticmethod
