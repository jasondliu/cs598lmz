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
f.__dict__['c'] = 'c'
f.__dict__['d'] = 'd'
f.__dict__['e'] = 'e'
f.__dict__['f'] = 'f'
f.__dict__['g'] = 'g'
f.__dict__['h'] = 'h'
f.__dict__['i'] = 'i'
f.__dict__['j'] = 'j'
f.__dict__['k'] = 'k'
f.__dict__['l'] = 'l'
f.__dict__['m'] = 'm'
f.__dict__['n'] = 'n'
f.__
