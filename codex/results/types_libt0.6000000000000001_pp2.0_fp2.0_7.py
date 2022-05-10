import types
types.MethodType(func, None, Foo)

class C(object):
    def __init__(self):
        self.x = 1
        self.y = 2

def f(self):
    return self.x + self.y

# Instances can have methods added to them
# after they are created, just like any other
# object attribute
c = C()
c.f = types.MethodType(f, c)
print c.f()
