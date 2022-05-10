import weakref
# Test weakref.ref() on instance objects.


class C:
    pass


for i in range(100):
    o = C()
    r = weakref.ref(o)
    del o
    r()

# weakref.ref() on user-defined types
