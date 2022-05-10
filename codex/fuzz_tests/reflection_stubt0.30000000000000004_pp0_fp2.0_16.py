fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# callable object
class A:
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

a = A()
a(1, 2, 3)

# callable class
class B:
    def __init__(self, x):
        self.x = x

    def __call__(self, *args, **kwargs):
        print(self.x, args, kwargs)

b = B(1)
b(2, 3, 4)

# callable instance
class C:
    def __init__(self, x):
        self.x = x

c = C(1)
c.__call__ = lambda *args, **kwargs: print(c.x, args, kwargs)
c(2, 3, 4)

# callable instance
class D:
    def __init__(self, x):
        self.x = x

d = D(1)
d.__call__ = lambda *args, **kwargs: print
