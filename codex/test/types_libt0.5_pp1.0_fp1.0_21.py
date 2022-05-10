import types
types.MethodType(lambda self, x: self.x + x, None, A)

# With __get__
def fget(self):
    return self.x + 1

A.f = property(fget)
A.f

# With __set__
def fset(self, value):
    self.x = value

A.f = property(None, fset)
a = A()
a.f = 3
a.x

# With __delete__
def fdel(self):
    del self.x

A.f = property(None, None, fdel)
a = A()
a.x = 3
del a.f
hasattr(a, 'x')

# With __get__ and __set__
