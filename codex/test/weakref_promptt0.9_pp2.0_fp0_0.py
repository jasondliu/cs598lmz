import weakref
# Test weakref.ref
try:
    w = weakref.ref(3)
except TypeError as e:
    print("TypeError:", e)
else:
    raise RuntimeError()

class A:
    pass
a = A()
w = weakref.ref(a)

try:
    w = weakref.ref(a, lambda x: None)
except TypeError as e:
    print("TypeError:", e)
else:
    raise RuntimeError()

try:
    w = weakref.ref(a, '')
except TypeError as e:
    print("TypeError:", e)
else:
    raise RuntimeError()

try:
    w = weakref.ref(a, 1, 2)
except TypeError as e:
    print("TypeError:", e)
else:
    raise RuntimeError()

from sys import getrefcount
w = weakref.ref(a)
if getrefcount(a) != 2:
    raise RuntimeError()

w = weakref.ref(a)
