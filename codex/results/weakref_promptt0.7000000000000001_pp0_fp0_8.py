import weakref
# Test weakref.ref to an object that implements __hash__
class A(object):
    def __hash__(self):
        return hash(self.__class__)
    def __eq__(self, other):
        return self is other

a = A()
r = weakref.ref(a)

# Test that weakref.ref on a class that implements __hash__, but not __eq__
# raises a TypeError
class B(object):
    def __hash__(self):
        return hash(self.__class__)

# Test that weakref.ref on a class that implements __eq__, but not __hash__
# raises a TypeError
class C(object):
    def __eq__(self, other):
        return self is other

b = B()
c = C()

try:
    weakref.ref(b)
except TypeError:
    pass
else:
    print("weakref.ref on class with __hash__, but not __eq__ should raise TypeError")

try:
    weakref.ref(c)
except TypeError:
    pass
