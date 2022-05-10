import weakref
# Test weakref.ref()

class C:
    def __init__(self, x):
        self.x = x

def f():
    c = C(42)
    r = weakref.ref(c)
    print(r())
    print(r() is c)
    print(r() is None)
    del c
    print(r() is None)

f()
