import weakref
# Test weakref.ref()
# This test case is based on the test case test_weakref.py in Python 2.7.1

# Test that weakref raises TypeError if its first argument is not safe to
# weakly reference.

# Weakrefs to old-style classes are not supported.

class C:
    pass

c = C()

try:
    weakref.ref(C)
except TypeError:
    print("TypeError")

try:
    weakref.ref(c)
except TypeError:
    print("TypeError")

try:
    weakref.ref(c, lambda: None)
except TypeError:
    print("TypeError")

try:
    weakref.ref(c, lambda: None, 1)
except TypeError:
    print("TypeError")
