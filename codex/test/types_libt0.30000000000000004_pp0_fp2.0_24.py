import types
types.MethodType(lambda self, x: x, None, A)

# These should all be valid
A.__dict__['m'].__get__(A(), A)
A.__dict__['m'].__get__(A(), A())
A.__dict__['m'].__get__(A(), None)
A.__dict__['m'].__get__(A(), 42)

# This should fail
A.__dict__['m'].__get__(A(), 'string')

# This should fail
A.__dict__['m'].__get__(A(), [])

# This should fail
A.__dict__['m'].__get__(A(), {})

# This should fail
A.__dict__['m'].__get__(A(), ())

# This should fail
A.__dict__['m'].__get__(A(), set())

# This should fail
A.__dict__['m'].__get__(A(), frozenset())

# This should fail
