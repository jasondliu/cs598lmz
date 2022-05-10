import weakref
# Test weakref.ref(class)

class E(Exception):
    pass

class A:
    pass

try:
    weakref.ref(E)
except TypeError:
    print('TypeError')
try:
    weakref.ref(A)
except TypeError:
    print('TypeError')
