import types
types.MethodType(lambda self: self.foo, None)

# This fails in CPython 2.7.5, but not in 3.4.2
class A(object):
    def foo(self):
        pass

A.foo.__get__(None, A)

# This fails in CPython 2.7.5, but not in 3.4.2
class A(object):
    def foo(self):
        pass

A.foo.__get__(A(), A)

# This fails in CPython 2.7.5, but not in 3.4.2
class A(object):
    def foo(self):
        pass

A.foo.__get__(A(), A)

# This fails in CPython 2.7.5, but not in 3.4.2
class A(object):
    def foo(self):
        pass

A.foo.__get__(A(), A)

# This fails in CPython 2.7.5, but not in 3.4.2
