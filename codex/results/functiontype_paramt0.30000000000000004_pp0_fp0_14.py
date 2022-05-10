from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# test_is_instance
class C: pass
class D(C): pass
isinstance(C(), C)
isinstance(D(), C)
isinstance(C(), D)
isinstance(D(), D)
isinstance('foo', str)
isinstance(b'foo', bytes)
isinstance(bytearray(b'foo'), bytes)
isinstance(range(5), range)
isinstance(5, int)
isinstance(5, (int, float))
isinstance(5, (float, int))

# test_is_not_instance
class C: pass
class D(C): pass
isnotinstance(C(), C)
isnotinstance(D(), C)
isnotinstance(C(), D)
isnotinstance(D(), D)
isnotinstance('foo', str)
isnotinstance(b'foo', bytes)
isnotinstance(bytearray(b'foo'), bytes)
isnotinstance(range(5), range)
isnotinstance(5, int)
isnotinstance
