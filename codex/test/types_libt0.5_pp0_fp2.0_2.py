import types
types.MethodType(test, None, Foo)

# test __dict__

class Foo:
    pass

f = Foo()
f.__dict__['x'] = 'x'
f.__dict__['y'] = 'y'
f.__dict__['z'] = 'z'
f.__dict__['a'] = 'a'
f.__dict__['b'] = 'b'
