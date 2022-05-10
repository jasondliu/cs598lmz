import weakref
# Test weakref.ref() with a class instance

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.ref() with a function

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())

del f
print(r())

# Test weakref.ref() with an integer

i = 42
r = weakref.ref(i)
print(r)
print(r())

del i
print(r())

# Test weakref.ref() with a string

s = "hello"
r = weakref.ref(s)
print(r)
print(r())

del s
print(r())

# Test weakref.ref() with a tuple

t = (1, 2,
