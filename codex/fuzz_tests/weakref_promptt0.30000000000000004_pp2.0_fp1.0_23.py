import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)
print(r() is p)
print(r() is o)

del o

print(r())
print(p)

print(r() is p)

try:
    print(p.foo)
except ReferenceError:
    print("ReferenceError")

try:
    p.foo = 12
except ReferenceError:
    print("ReferenceError")

try:
    del p.foo
except ReferenceError:
    print("ReferenceError")

try:
    p()
except TypeError:
    print("TypeError")

try:
    p(1)
except TypeError:
    print("TypeError")

try:
    p(1, 2)
except TypeError:
    print("TypeError")

try:
    p(1, 2, 3)
except TypeError:
    print("Type
