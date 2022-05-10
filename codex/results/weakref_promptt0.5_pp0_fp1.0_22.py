import weakref
# Test weakref.ref(int)
ref = weakref.ref(42)
assert ref() == 42
# Test weakref.ref(tuple)
tup = (1, 2, 3)
ref = weakref.ref(tup)
assert ref() == tup
tup = None
# Test weakref.ref(set)
s = set([1, 2, 3])
ref = weakref.ref(s)
assert ref() == s
s = None
# Test weakref.ref(dict)
d = dict(a=1, b=2, c=3)
ref = weakref.ref(d)
assert ref() == d
d = None
# Test weakref.ref(list)
l = [1, 2, 3]
ref = weakref.ref(l)
assert ref() == l
l = None
# Test weakref.ref(str)
s = "test"
ref = weakref.ref(s)
assert ref() == s
s = None
# Test weakref.ref(bool)
ref = weakref.ref(True)
assert ref() is True

