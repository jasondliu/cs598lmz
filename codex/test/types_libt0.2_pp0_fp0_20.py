import types
types.MethodType(foo, None, None)

# The following should not crash
class A(object):
    def __init__(self):
        self.foo = types.MethodType(foo, self)

a = A()
a.foo()

# The following should not crash
class B(object):
    def __init__(self):
        self.foo = types.MethodType(foo, self, None)

b = B()
b.foo()

# The following should not crash
class C(object):
    def __init__(self):
        self.foo = types.MethodType(foo, self, None, None)

c = C()
c.foo()

# The following should not crash
class D(object):
    def __init__(self):
        self.foo = types.MethodType(foo, self, None, None, None)

d = D()
d.foo()

# The following should not crash
