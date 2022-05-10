import weakref
# Test weakref.ref with a class that has a __del__ method.
# This is a regression test for SF bug #534135.

class C:
    def __del__(self):
        pass

def f():
    c = C()
    ref = weakref.ref(c)
    del c
    return ref

r = f()
print(r())
