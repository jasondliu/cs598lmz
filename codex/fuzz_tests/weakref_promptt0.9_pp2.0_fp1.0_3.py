import weakref
# Test weakref.ref(1,'foo') and weakref.ref(1.345,'foo')
for x in 1, 1.345:
    ref = weakref.ref(x, lambda x: None)
    assert ref() == x
    x = None
    assert ref() is None
