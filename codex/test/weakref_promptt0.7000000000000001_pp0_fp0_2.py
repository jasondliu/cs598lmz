import weakref
# Test weakref.ref() and weakref.proxy() with a class instance.

class C:
    pass

c = C()
try:
    weakref.ref(c)
except TypeError:
    print('TypeError')

try:
    weakref.proxy(c)
except TypeError:
    print('TypeError')
