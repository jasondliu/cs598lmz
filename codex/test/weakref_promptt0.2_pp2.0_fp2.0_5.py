import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)
print(r() is None)

del o
print(r() is None)

# Test weakref.ref() with a function.

def f():
    pass

r = weakref.ref(f)

print(r())
print(r() is f)
print(r() is None)

del f
print(r() is None)

# Test weakref.ref() with a built-in function.

r = weakref.ref(len)

print(r())
print(r() is len)
print(r() is None)

del len
print(r() is None)

# Test weakref.ref() with a built-in method.

r = weakref.ref(''.join)

print(r())
print(r() is ''.join)
print(r() is None)

del str
