import weakref
# Test weakref.ref() with a class instance.
import weakref

class C(object):
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)
print(r() is None)

print('-' * 60)

# Test weakref.ref() with a function.
import weakref

def f():
    pass

r = weakref.ref(f)
print(r)
print(r())
print(r() is f)
print(r() is None)

print('-' * 60)

# Test weakref.ref() with an int.
import weakref

i = 42
r = weakref.ref(i)
print(r)
print(r())
print(r() is i)
print(r() is None)

print('-' * 60)

# Test weakref.ref() with a str.
import weakref

s = 'abc'
r = weakref.ref(s)
print(r)
