import weakref
# Test weakref.ref with a class that implements enough of a __del__ method to
# be troublesome.

class ObjectWithDel:
    def __del__(self):
        pass


def f():
    o = ObjectWithDel()
    ref = weakref.ref(o)
    o = 1


f()
del ObjectWithDel  # try to keep refcounts of ObjectWithDel instances non-zero
