import types
types.MethodType(lambda self: None, None, D)

# Test that the __dict__ of a class is writable
D.__dict__['foo'] = 'bar'

# Test that the __dict__ of a class is writable via the class
D.foo = 'bar'

# Test that the __dict__ of a class is writable via the instance
D().foo = 'bar'

# Test that the __dict__ of a class is writable via type.__setattr__
type.__setattr__(D, 'foo', 'bar')

# Test that the __dict__ of a class is writable via object.__setattr__
object.__setattr__(D, 'foo', 'bar')

# Test that the __dict__ of a class is writable via the metaclass
type.__setattr__(type(D), 'foo', 'bar')

# Test that the __dict__ of a class is writable via type.__setattr__
type.__setattr__(type, 'foo', 'bar')

# Test that the __dict__ of a
