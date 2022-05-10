import weakref
# Test weakref.ref() on a class instance.
class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())

del c
print(r)
print(r())

# Test weakref.ref() on a function.
def f():
    pass

r = weakref.ref(f)
print(r)
print(r())

del f
print(r)
print(r())

# Test weakref.ref() on a builtin function.
r = weakref.ref(len)
print(r)
print(r())

# Test weakref.ref() on a method.
class C:
    def m(self):
        pass

c = C()
r = weakref.ref(c.m)
print(r)
print(r())

del c
print(r)
print(r())

# Test weakref.ref() on a bound method.
class C:
    def m(self):
        pass

c = C()
r = weakref.ref(c
