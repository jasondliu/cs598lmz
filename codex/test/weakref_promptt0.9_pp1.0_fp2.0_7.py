import weakref
# Test weakref.ref(). It doesn't work on default __main__.
# See test__main__.py.
x = []
x.append(weakref.ref(x))
