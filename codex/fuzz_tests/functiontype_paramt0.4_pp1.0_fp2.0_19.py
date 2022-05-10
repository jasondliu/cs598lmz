from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'foo'))

# Test that we can call __new__ on a type with a non-tuple __args__
# attribute.
class C:
    __args__ = None
    def __new__(cls, *args):
        return object.__new__(cls)
C()

# Test that we can call __new__ on a type with a tuple __args__
# attribute.
class D:
    __args__ = ()
    def __new__(cls, *args):
        return object.__new__(cls)
D()

# Test that we can call __new__ on a type with a tuple __args__
# attribute that contains a non-type.
class E:
    __args__ = (None,)
    def __new__(cls, *args):
        return object.__new__(cls)
E()

# Test that we can call __new__ on a type with a tuple __args__
# attribute that contains a type.
class F:
    __args__ = (object,)
