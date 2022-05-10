import weakref
# Test weakref.ref(obj)

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())
print(r() is f)

# Test weakref.ref(obj, callback)

def bye():
    print("Gone with the wind...")

f = Foo()
r = weakref.ref(f, bye)
print(r)
print(r())
print(r() is f)

del f
print(r())

# Test weakref.WeakKeyDictionary

class Foo:
    pass

f1 = Foo()
f2 = Foo()
f3 = Foo()

d = weakref.WeakKeyDictionary()
d[f1] = 1
d[f2] = 2
d[f3] = 3

print(d[f1])
print(d[f2])
print(d[f3])

del f1

print(d[f2])
print(d[f3])

del f2

print(d[f3])

