import weakref
# Test weakref.ref()

def foo():
    pass

r = weakref.ref(foo)
print(r)
print(r())

def bar(x):
    pass

r = weakref.ref(bar)
print(r)
print(r(6))
