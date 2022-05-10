import weakref
# Test weakref.ref() on a plain old class.
class C:
    pass


obj = C()
r = weakref.ref(obj)
print repr(r())
print r() is obj
del obj
print r()
# Test weakref.ref() on a class with a __del__ method.
class D:
    def __init__(self):
        self.n = 1

    def __del__(self):
        print self.n


obj = D()
r = weakref.ref(obj)
print repr(r())
print r() is obj
obj.n = 2
del obj
print r()
# Test weakref.ref() on a class with a __weakref__ slot.
class E:
    pass


obj = E()
obj.__weakref__ = 1
try:
    r = weakref.ref(obj)
except TypeError:
    pass
else:
    print 'expected TypeError not raised'
# Test weakref.ref() on a class with a __proto__ slot.
class F:
    pass


obj = F()
obj.__
