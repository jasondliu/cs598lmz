import weakref
# Test weakref.ref() fails with builtins
try:
    weakref.ref(object)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test weakref.ref() fails with non-weak referencable objects
try:
    weakref.ref(object())
except TypeError:
    print('SKIP')
    raise SystemExit

# Test weakref.proxy() fails with builtins
try:
    weakref.proxy(object)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test weakref.proxy() fails with non-weak referencable objects
try:
    weakref.proxy(object())
except TypeError:
    print('SKIP')
    raise SystemExit
