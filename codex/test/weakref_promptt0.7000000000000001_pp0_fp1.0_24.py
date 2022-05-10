import weakref
# Test weakref.ref on names in __builtin__.
import __builtin__
for name in dir(__builtin__):
    ref = weakref.ref(getattr(__builtin__, name))
    # If we can get back to the original object, then it can't be a weak
    # reference.
