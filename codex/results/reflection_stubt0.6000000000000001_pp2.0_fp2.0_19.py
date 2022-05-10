fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())

# ctypes

# C
class C(object):
    def __init__(self):
        self.__dict__ = {'a': 1}

c = C()
c.b = 2
print(c.a)
print(c.b)

# X
class X(object):
    def __getattr__(self, name):
        return 42

x = X()
print(x.a)
print(x.b)

# Y
class Y(object):
    def __getattribute__(self, name):
        return 42

y = Y()
print(y.a)
print(y.b)

# Z
class Z(object):
    def __getattr__(self, name):
        return 42
    def __getattribute__(self, name):
        return 42

z = Z()
print(z.a)
print(z.b)

# Z2
class Z2(object):
    def __getattribute__(self, name):
        return 42
   
