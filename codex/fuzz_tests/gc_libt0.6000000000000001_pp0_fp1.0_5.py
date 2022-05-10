import gc, weakref

class A(object):
    def __init__(self):
        self.a = 1
    def f(self):
        return self.a

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = 2
    def g(self):
        return self.b

class C(B):
    def __init__(self):
        B.__init__(self)
        self.c = 3
    def h(self):
        return self.c

class D(C):
    def __init__(self):
        C.__init__(self)
        self.d = 4
    def i(self):
        return self.d

# create a circular reference
foo = A()
foo.next = foo

# create a reference to a class method
def f(obj):
    return obj.f()
foo.meth = f.__get__(foo)

# create a reference to an instance method
bar = B()
bar.meth = bar.g


