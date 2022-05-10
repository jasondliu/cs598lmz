import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(type(r) is weakref.ReferenceType)
print(type(p) is weakref.ProxyType)

print(r() is o)
print(p is o)
print(r() == o)
print(p == o)

print(r() is p)
print(r() == p)

print(p.__class__ is C)
print(r().__class__ is C)

try:
    print(p.abc)
except AttributeError:
    print("AttributeError")

try:
    print(r().abc)
except AttributeError:
    print("AttributeError")

try:
    print(p.abc)
except ReferenceError:
    print("ReferenceError")

try:
    print(r().abc)
except ReferenceError:
    print("ReferenceError")

del o

try:
    print
