import weakref
# Test weakref.ref() on an instance of a classic class.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
del o
print(r())
# Test weakref.ref() on an instance of a new-style class.

class C(object):
    pass

o = C()
r = weakref.ref(o)
print(r())
del o
print(r())
# Test weakref.ref() on a tuple.

t = (1, 2, 3)
r = weakref.ref(t)
print(r())
del t
print(r())
# Test weakref.ref() on a list.

l = [1, 2, 3]
r = weakref.ref(l)
print(r())
del l
print(r())
# Test weakref.ref() on a dict.

d = {1: 1, 2: 2, 3: 3}
r = weakref.ref(d)
print(r())
del d
print(r())
# Test weakref.ref()
