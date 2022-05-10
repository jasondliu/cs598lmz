import gc, weakref

class A(object):
    def __init__(self):
        self.b = B()
        self.c = C()

class B(object):
    def __init__(self):
        self.a = A()

class C(object):
    def __init__(self):
        self.a = A()

a = A()
b = weakref.ref(a.b)
c = weakref.ref(a.c)

del a
gc.collect()

print b()
print c()
</code>

