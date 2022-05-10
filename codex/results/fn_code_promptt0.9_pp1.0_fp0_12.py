fn = lambda: None
# Test fn.__code__.__eq__(self) handling.
class with_code:
    def __init__(self, code):
        self.code = code
tuple.__eq__ = with_code(tuple.__code__)
del with_code
class M:
    pass

assert M.__name__ == 'M'
assert M.__dict__ is M.__dict__
class M:
    def meth():
        pass

M.foo = 2
M.__module__ = 'foo'
assert M.foo == 2
assert M.meth.__module__ == 'foo'
assert M.__module__ == 'foo'

# Changes in a superclass are immediately visible in a subclass,
# even if the subclass was created before the changes.

class M(object):
    pass

class N(M):
    pass

M.foo = 2
assert N.foo == 2
del M.foo
class M(object):
    pass

M.foo = 2
class N(M):
    pass

assert N.foo == 2
del M.foo

