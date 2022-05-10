import weakref
# Test weakref.ref() for callable objects

class C:
    def __call__(self):
        return 42

c = C()
r = weakref.ref(c)
print r()

c = None
print r()

class C:
    def __init__(self, n):
        self.n = n
    def __call__(self):
        return self.n

c = C(42)
r = weakref.ref(c)
print r()

c = None
print r()
