import types
# Test types.FunctionType
def foo(a):
    return a
def f():
    a = 10
    b = foo(a)
    return b

assert f() == 10

def f():
    a = 10
    b = foo
    return b(a)

assert f() == 10

def f():
    a = 10
    b = foo(a)
    return b(a)

assert f() == 10

def f():
    a = 10
    b = foo
    return b(a)(a)

assert f() == 10

def f():
    a = 10
    b = foo(a)
    return b(a)(a)

assert f() == 10

def foo(a):
    return a
class A:
    pass

a = A()

# Test printing of class instances
assert str(a) == '<A>'

a.foo = foo

assert str(a.foo) == 'foo'

assert isinstance(a.foo, types.FunctionType)

assert str(a.foo(a)) ==
