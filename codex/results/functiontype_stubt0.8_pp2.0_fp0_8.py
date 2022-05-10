from types import FunctionType
a = (x for x in [1])
b = None
c, d = {}, ()
e = FunctionType
f = 1.23


# repr
print repr(a), repr(b), repr(c), repr(d), repr(e), repr(f)
# type
print type(a), type(b), type(c), type(d), type(e), type(f)
# isinstance
print isinstance(a, GeneratorType), isinstance(b, NoneType), isinstance(c, dict), isinstance(d, tuple), isinstance(e, type(lambda: 0)), isinstance(f, float)
# is
print a is b, b is c, c is d, e is f
