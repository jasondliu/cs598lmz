import weakref
# Test weakref.ref(None)
weakref.ref(None)

# Test weakref.ref(1)
weakref.ref(1)

# Test weakref.ref(1.0)
weakref.ref(1.0)

# Test weakref.ref("foo")
weakref.ref("foo")

# Test weakref.ref(u"bar")
weakref.ref(u"bar")

# Test weakref.ref(True)
weakref.ref(True)

# Test weakref.ref(False)
weakref.ref(False)

# Test weakref.ref(Ellipsis)
weakref.ref(Ellipsis)

# Test weakref.ref(())
weakref.ref(())

# Test weakref.ref(NotImplemented)
weakref.ref(NotImplemented)

# Test weakref.ref(object())
weakref.ref(object())

# Test weakref.ref(object)
weakref.ref(object)

# Test weakref.ref(weakref)
