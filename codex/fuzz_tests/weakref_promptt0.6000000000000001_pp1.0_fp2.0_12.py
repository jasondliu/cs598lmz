import weakref
# Test weakref.ref() to see if it returns a weak reference
# instead of a strong reference
import sys
if weakref.ref(int)() is int:
    raise Exception("weakref.ref() does not return a weak reference")
# Test weakref.WeakKeyDictionary() to see if it accepts weak references
# as keys.
try:
    weakref.WeakKeyDictionary({int: 1})
except:
    raise Exception("weakref.WeakKeyDictionary() does not accept weak references as keys")
try:
    weakref.WeakKeyDictionary({weakref.ref(int): 1})
except:
    raise Exception("weakref.WeakKeyDictionary() does not accept weak references as keys")

# Test weakref.WeakValueDictionary() to see if it accepts weak references
# as values.
try:
    weakref.WeakValueDictionary({1: int})
except:
    raise Exception("weakref.WeakValueDictionary() does not accept weak references as values")
try:
    weakref.WeakValueDictionary({1: weakref.ref(int)})
except:
    raise Exception("
