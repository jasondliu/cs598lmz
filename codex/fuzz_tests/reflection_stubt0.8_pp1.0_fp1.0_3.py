fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class C:
    __slots__ = 'a', 'b'


del C.a
del C.b

with open('__main__.py', 'rb') as f:
    mod = f.read()

code = compile(mod, '__main__.py', 'exec')

d = {'f1': lambda: None,
     'f2': lambda x: None,
     'f3': lambda x, y: None,
     'f4': lambda *args: None,
     'f5': lambda **kwargs: None,
     'f6': lambda x=1, y=2: None,
     'f7': lambda *, x=1, y=2: None,
     'f8': lambda x, y=1, z=2: None,
     'f9': lambda x, y=1, *z: None,
     'f10': lambda x, y=1, *z, **kwargs: None,
     'f11': lambda x=1, **kwargs: None,
     }

res =
