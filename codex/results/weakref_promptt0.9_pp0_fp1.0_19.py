import weakref
# Test weakref.ref separately, to find unexpected side effects.

class X:
    pass

def callback(wr):
    print("callback on", wr)

wr = weakref.ref(X(), callback)
print("created", wr)
del X
