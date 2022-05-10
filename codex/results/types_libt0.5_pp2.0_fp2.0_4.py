import types
types.MethodType(lambda self: None, None, C)

# Test that the __slots__ attribute is copied to the new class.
class D(C):
    __slots__ = ()

# Test that the __slots__ attribute is copied to the new class.
class E(C):
    __slots__ = 'a',

# Test that the __slots__ attribute is copied to the new class.
class F(C):
    __slots__ = 'a', 'b'

# Test that the __slots__ attribute is copied to the new class.
class G(C):
    __slots__ = ('a',)

# Test that the __slots__ attribute is copied to the new class.
class H(C):
    __slots__ = ('a', 'b')
