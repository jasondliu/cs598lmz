import weakref
# Test weakref.ref in general
def callback(r):
    print(2)
    print(r)

object = weakref.ref(object(), callback)
print(1)
print(object)


# Test weakref.ref behavior and callback.
# Expect callbacks to not happen on reference destruction.
# Only the finalizer running, which runs the sequence of callbacks
# registered with the reference object. 
def callback(r):
    print(2)
    print(r)

object = weakref.ref(object(), callback)
print(1)
print(object)
del object
