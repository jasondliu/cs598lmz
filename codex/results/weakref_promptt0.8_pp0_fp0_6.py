import weakref
# Test weakref.ref in purely functional mode
def f(): pass
wr = weakref.ref(f)
print wr() is f
