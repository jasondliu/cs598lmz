import weakref
# Test weakref.ref
class B(object):
    def __init__(self):
        self.x = 42

class C(object):
    def __init__(self):
        self.b = B()

class D(object):
    def __init__(self):
        self.c = C()

def f(x):
    print x()

d = D()
c = weakref.ref(d.c, f)
print c
print c()
print c().b
print c().b.x
print '-'*20
d = None
print c()
print c().b
print c().b.x
