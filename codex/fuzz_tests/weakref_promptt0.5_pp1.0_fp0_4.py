import weakref
# Test weakref.ref(obj)

# Create a weak reference to a function
def f():
    pass
r = weakref.ref(f)
# Test weakref.proxy(obj)

# Create a weak reference to a function
def f():
    pass
p = weakref.proxy(f)
# Test weakref.getweakrefcount(obj)

# Create a weak reference to a function
def f():
    pass
r = weakref.ref(f)
print(weakref.getweakrefcount(f))
# Test weakref.getweakrefs(obj)

# Create a weak reference to a function
def f():
    pass
r = weakref.ref(f)
print(weakref.getweakrefs(f))
# Test weakref.ReferenceType

# Create a weak reference to a function
def f():
    pass
r = weakref.ref(f)
print(type(r))
# Test weakref.ReferenceType.__call__()

# Create a weak reference to a function
def f():
    pass
r = weakref.ref(f)
