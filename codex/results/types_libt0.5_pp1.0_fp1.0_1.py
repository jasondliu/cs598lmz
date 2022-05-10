import types
types.MethodType(foo, None, None)

# Test for issue #5
class A(object):
    def foo(self):
        return "foo"

class B(A):
    pass

def bar(self):
    return "bar"

b = B()
b.foo = types.MethodType(bar, b, B)
assert b.foo() == "bar"

# Test for issue #6
def foo():
    pass

types.MethodType(foo, None, None)

# Test for issue #9
def foo(self):
    pass

class A(object):
    pass

a = A()
a.foo = types.MethodType(foo, a, A)
assert a.foo() is None

# Test for issue #10
def foo(self):
    pass

class A(object):
    pass

a = A()
a.foo = types.MethodType(foo, a, A)
assert a.foo() is None

# Test for issue #11
def foo(self):
    return "foo"


