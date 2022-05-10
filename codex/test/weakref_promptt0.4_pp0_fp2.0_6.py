import weakref
# Test weakref.ref() with a class that has a __del__ method.

class C:
    def __del__(self):
        pass

r = weakref.ref(C())
r()
r() is None
