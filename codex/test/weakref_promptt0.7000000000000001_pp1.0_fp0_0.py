import weakref
# Test weakref.ref not implemented on class
try:
    class foo(object):
        pass
    f = weakref.ref(foo())
except TypeError:
    print('SKIP')
    raise SystemExit

# Test weakref.proxy not implemented on class
try:
    class foo(object):
        pass
    f = weakref.proxy(foo())
except TypeError:
    print('SKIP')
    raise SystemExit
