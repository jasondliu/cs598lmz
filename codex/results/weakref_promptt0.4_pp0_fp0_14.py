import weakref
# Test weakref.ref() with a class that has a __del__ method.

class Foo:
    def __init__(self, i):
        self.i = i
        self.d = weakref.ref(self)

    def __del__(self):
        print "deleting Foo instance", self.i

f = Foo(1)
f.d()
del f

f = Foo(2)
d = weakref.ref(f)
f.d()
del f
print d()

f = Foo(3)
d = weakref.ref(f)
f.d()
del f
print d()

f = Foo(4)
d = weakref.ref(f)
f.d()
del f
print d()

f = Foo(5)
d = weakref.ref(f)
f.d()
del f
print d()

f = Foo(6)
d = weakref.ref(f)
f.d()
del f
print d()

f = Foo(7)
d = weakref.ref(f)

