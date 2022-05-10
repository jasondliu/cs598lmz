import weakref
# Test weakref.ref
r = weakref.ref(lambda: None)
r()
r
r()
r
# Test weakref.WeakKeyDictionary
a = weakref.WeakKeyDictionary()
a[1] = 1
a
a[2] = 2
a
