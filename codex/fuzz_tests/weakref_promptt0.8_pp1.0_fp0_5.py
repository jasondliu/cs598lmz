import weakref
# Test weakref.ref()
# This should fail, since weak references cannot be created for types
try:
    weakref.ref(bool)
except TypeError:
    print("TypeError")

try:
    weakref.ref(type)
except TypeError:
    print("TypeError")
