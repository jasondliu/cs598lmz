import weakref
# Test weakref.ref()
try:
    weakref.ref(1)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test weakref.ref() with a callable
def f():
    return 1

r = weakref.ref(f)
print(r())

# Test weakref.ref() with a proxy
class C:
    pass

c = C()
r = weakref.ref(c)
print(r())

# Test weakref.proxy() with a callable
def f():
    return 1

r = weakref.proxy(f)
print(r())

# Test weakref.proxy() with a proxy
class C:
    pass

c = C()
r = weakref.proxy(c)
print(r)
