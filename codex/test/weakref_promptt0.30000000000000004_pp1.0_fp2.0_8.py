import weakref
# Test weakref.ref() with a class instance.
class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.ref() with a class instance method.
class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
print(r)
print(r())
print(r() is o.f)
print(r() is None)

# Test weakref.ref() with a class instance method.
class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
print(r)
print(r())
print(r() is o.f)
print(r() is None)

# Test weakref.ref() with a class instance method.
class C:
    def f(self):
        pass

o = C()
r = weakref.ref(o.f)
