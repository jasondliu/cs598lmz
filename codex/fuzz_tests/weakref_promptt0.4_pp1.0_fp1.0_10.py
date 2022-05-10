import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)

del c
print(r())

# Test weakref.ref(None)

try:
    weakref.ref(None)
except TypeError:
    print("TypeError")

# Test weakref.ref(123)

try:
    weakref.ref(123)
except TypeError:
    print("TypeError")

# Test weakref.ref(1.23)

try:
    weakref.ref(1.23)
except TypeError:
    print("TypeError")

# Test weakref.ref("abc")

try:
    weakref.ref("abc")
except TypeError:
    print("TypeError")

# Test weakref.ref(b"abc")

try:
    weakref.ref(b"abc")
except TypeError:
    print("TypeError")

# Test weakref.ref(bytearray(b
