import weakref
# Test weakref.ref() for callable objects

class C:
    def __call__(self):
        return 42

c = C()
r = weakref.ref(c)
