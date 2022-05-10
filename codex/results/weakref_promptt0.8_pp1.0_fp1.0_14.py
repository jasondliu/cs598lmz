import weakref
# Test weakref.ref(lambda x: None) and weakref.ref(functools.partial(...))
ref = weakref.ref
ref(lambda x: None)  # should succeed
ref(functools.partial(int, base=10))  # should succeed
