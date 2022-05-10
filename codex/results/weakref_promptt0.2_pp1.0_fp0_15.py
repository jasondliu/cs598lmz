import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(o2)

o = o2 = None
print(r())
print(r2())

# Test weakref.ref() with a function.

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())

f2 = f
r2 = weakref.ref(f2)
print(r2)
print(r2())

f = f2 = None
print(r())
print(r2())

# Test weakref.ref() with a builtin function.

r = weakref.ref(len)
print(r)
print(r())

len2 = len
r2 = weakref.ref(len2)
print(r2)
print(
