import weakref
# Test weakref.ref(a)() with a being an old style class.

class C:

    def __init__(self, v):
        self.__v = v

    def value(self):
        return self.__v

x = C(42)
r = weakref.ref(x)
print x.value()
del x
print r().value()
