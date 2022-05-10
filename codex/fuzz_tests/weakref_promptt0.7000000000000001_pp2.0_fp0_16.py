import weakref
# Test weakref.ref() on a tuple:

class MyTuple(tuple):
    pass

t = MyTuple((1, 2.0))
r = weakref.ref(t)
print r(), repr(r())

t = MyTuple((3, 4.0))
print r(), repr(r())
