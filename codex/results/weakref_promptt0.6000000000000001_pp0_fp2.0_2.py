import weakref
# Test weakref.ref()

# Create a weak reference to a function
def f():
    return 42
wf = weakref.ref(f)

# The function is still available
assert f() == 42

# Delete the function, and check that the weak reference to it is dead
del f
assert wf() is None
# Test weakref.proxy()

# Create a weak reference to a function
def f():
    return 42
wf = weakref.proxy(f)

# The function is still available
assert wf() == 42

# Delete the function, and check that the weak reference to it is dead
del f
try:
    wf()
except ReferenceError:
    pass
else:
    assert False, "expected a ReferenceError"
# Test weakref.WeakValueDictionary()

class C:
    pass

wvd = weakref.WeakValueDictionary()

# Create an object
c = C()

# Store a reference to it in the weak value dictionary
wvd['a'] = c

# The object is still available
assert wvd['a'] is c

