import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: None)
assert r2() is o2

try:
    weakref.ref(C)
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    weakref.ref(1)
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    weakref.ref("foo")
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    weakref.ref(b"foo")
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    weakref.ref(1.5)
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    weakref.ref(1j)
except TypeError:
    pass

