import weakref
# Test weakref.ref() with a class instance.
class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
del o
print(r())

# Test weakref.ref() with a function.
def f():
    pass

r = weakref.ref(f)
print(r)
print(r())
print(r() is f)
del f
print(r())

# Test weakref.ref() with an integer.
i = 42
r = weakref.ref(i)
print(r)
print(r())
print(r() is i)
del i
print(r())

# Test weakref.ref() with a string.
s = "abc"
r = weakref.ref(s)
print(r)
print(r())
print(r() is s)
del s
print(r())

# Test weakref.ref() with a tuple.
t = (1, 2, 3)
r = weakref.ref(t)
print
