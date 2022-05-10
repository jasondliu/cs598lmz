import weakref
# Test weakref.ref
class MyClass(object):
    def __init__(self): 
        pass

    def __del__(self):
        print "Instance deleted"

ref = weakref.ref(MyClass())
assert ref() is None

# Test weakref.WeakKeyDictionary
class MyClass2(object):
    pass
inst1 = MyClass2()
inst2 = MyClass2()

wkd = weakref.WeakKeyDictionary()
wkd[inst1] = 1
assert inst1 in wkd
wkd[inst2] = 2
wkd.clear()
assert inst1 not in wkd
assert inst2 not in wkd

# Test weakref.WeakValueDictionary
wvd = weakref.WeakValueDictionary()
wvd["s"] = inst1
assert inst1 in wvd.values()
wvd["d"] = inst2
wvd.clear()
assert inst1 not in wvd.values()
assert inst2 not in wvd.values()

# Test weakref to builtin types
# Weak reference to an array
import array

