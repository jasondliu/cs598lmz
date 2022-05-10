import types
types.MethodType(lambda self: None, None, D)

# Test that the __dict__ of a class is writable
D.__dict__['foo'] = 'bar'

# Test that the __dict__ of a class is writable via the class
D.foo = 'bar'
