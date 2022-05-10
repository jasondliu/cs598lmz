from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# Test __repr__
assert repr(FunctionType(lambda x: x, globals(), 'foo')) == \
        '<function foo at 0x%x>' % id(FunctionType(lambda x: x, globals(), 'foo'))

# Test __str__
assert str(FunctionType(lambda x: x, globals(), 'foo')) == '<function foo at 0x%x>' % id(FunctionType(lambda x: x, globals(), 'foo'))

# Test __get__
def f(self, x):
    return x

class A(object):
    f = f

a = A()
assert a.f(1) == 1
assert A.f(a, 1) == 1

# Test __call__
def f(x):
    return x

assert f(1) == 1

# Test __code__
def f(x):
    return x

assert f.__code__.co_argcount == 1

# Test __defaults__
def
