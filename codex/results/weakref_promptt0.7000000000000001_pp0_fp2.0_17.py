import weakref
# Test weakref.ref()
import pickle

class MyClass(object):
    pass

inst = MyClass()
w = weakref.ref(inst)

# The following line raises AttributeError, because
# the attribute '__weakref__' is not set:
# inst.__weakref__ = w

# The following line works fine:
MyClass.__weakref__ = w

# The following line also raises AttributeError,
# because the attribute '__weakref__' is now read-only:
# inst.__weakref__ = w

# Let's try writing a pickle now...
s = pickle.dumps(inst)

# Now, let's unpickle the instance, and see if the
# attribute '__weakref__' was restored:
inst2 = pickle.loads(s)
inst2.__weakref__
