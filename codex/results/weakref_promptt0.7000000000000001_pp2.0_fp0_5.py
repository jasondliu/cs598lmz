import weakref
# Test weakref.ref(x) is x
print(weakref.ref(42) is 42)
# Test weakref.ref(x)() is x
print(weakref.ref(42)() is 42)
w = weakref.ref(42)
# Test repr
print(repr(w))

# Test repr() on a proxy
w = weakref.ref(42)
p = w.__repr__
print(p())

# Test str() on a proxy
w = weakref.ref(42)
p = w.__str__
print(p())

# Test hash() on a proxy
w = weakref.ref(42)
p = w.__hash__
print(p())

# Test bool() on a proxy
w = weakref.ref(42)
p = w.__bool__
print(p())

# Test getattr() on a proxy
w = weakref.ref(42)
print(getattr(w, "__str__")())

# Test del on a proxy
w = weakref.ref(42)
del w

# Test
