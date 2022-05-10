import weakref
# Test weakref.ref(obj), where obj is hashable
print "Testing creation and use of weak references to hashable objects"

# subtype of a built-in type
class D(dict):
    def __hash__(self):
        return id(self)
d = D({'a': 1, 'b': 2})
r = weakref.ref(d)
print type(r), r() is d
print r() == d
d['c'] = 3
print r().keys()
del d
print r()


# user-defined class with a custom __hash__ method
class C:
    def __init__(self, a):
        self.a = a
    def __hash__(self):
        return id(self)
    def __eq__(self, other):
        #print "comparing", id(self), id(other), self.a, other.a
        return self.a == other.a
    def __repr__(self):
        return "<C %d>" % (id(self))
c1 = C(1)
c2 = C(2)


