import weakref
# Test weakref.ref(x)
class Foo:
    pass
foo = Foo()
r = weakref.ref(foo)
print(r)
print(r())
print(r() is foo)

# Test weakref.ref(x, cb)

def mycallback(r):
    print("mycallback(%s)" % r)

def mycallback2(r):
    print("mycallback2(%s)" % r)

def mycallback3(r):
    print("mycallback3(%s)" % r)

r = weakref.ref(foo, mycallback)
print(r)
print(r())
print(r() is foo)

# Test weakref.ref(x, cb, cb2)
r = weakref.ref(foo, mycallback, mycallback2)
print(r)
print(r())
print(r() is foo)

# Test weakref.ref(x, cb, cb2, cb3)
r = weakref.ref(foo, mycallback, mycallback2, mycallback3)
print(
