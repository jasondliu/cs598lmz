import weakref
# Test weakref.ref()
w = weakref.ref(dict)
assert isinstance(w, weakref.ref)
assert w() is dict
assert w() is not dict
# Test weakref.WeakValueDictionary
min_ver = (3, 4)
max_ver = (3, 5)
if sys.version_info[:2] in range(min_ver[:2], max_ver[:2]):
    raise RuntimeError("This test is valid only between " + " and ".join(sys.version_info[:2]))
unknown_type = type('unknown', (object,), {})
d1 = weakref.WeakValueDictionary({'whater': unknown_type})
d2 = weakref.WeakValueDictionary({'whater': dict})
assert len(d1) == 1
assert len(d2) == 1
# Do not allow WeakValueDictionary to contain itself
try:
    weakref.WeakValueDictionary({'whater': d1})
except TypeError:
    pass
else:
    raise RuntimeError("WeakValueDictionary contains itself")
# Create an
