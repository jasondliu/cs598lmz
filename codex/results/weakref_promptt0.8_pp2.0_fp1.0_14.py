import weakref
# Test weakref.ref() with a callable (weakref.WeakMethod)

def f():
    pass


class C:
    def g(self):
        pass

def h():
    pass

class D:
    def __init__(self):
        self.r = weakref.ref(h)

d = D()
print(d.r())

# Test weakref.ref() with a non-callable
def g():
    pass

class C:
    def g():
        pass

r = weakref.ref(g)
print(r)

# Test weakref.WeakMethod, a weak reference to a bound method
class C:
    def f(self):
        pass

# Non-weak reference to bound method
c = C()
m = c.f

# Weak reference to bound method
w = weakref.WeakMetho
