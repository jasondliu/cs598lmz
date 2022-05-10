import weakref
# Test weakref.ref(s) is an instance of the type, but then only
# a weakref.ReferenceType, not a weakref.WeakSet in this case.
import weakref
import sys
try:
    from weakrefset import WeakSet
except ImportError:
    WeakSet = None

if WeakSet is None:
    raise Exception("Could not import weakrefset.weakset")

class MyInt(int):
    pass

class MyStr(str):
    pass

