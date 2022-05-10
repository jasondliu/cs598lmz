import weakref
# Test weakref.ref() on a tuple:

class MyTuple(tuple):
    pass

t = MyTuple((1, 2.0))
r = weakref.ref(t)
