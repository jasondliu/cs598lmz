import weakref
# Test weakref.ref and weakref.WeakKeyDictionary
ref_to_obj = weakref.ref(Object())
print ref_to_obj  # weakref(<__main__.Object object at 0x7f0dc917d750>)

# Create a WeakKeyDictionary and add an entry
dict_with_weak_keys = weakref.WeakKeyDictionary()
dict_with_weak_keys[Object()] = 'I belong to object in WeakKeyDictionary'

# Test that ref_to_obj is equivalent to the original obj
assert Object.from_id(ref_to_obj().__id__()) is ref_to_obj()
# Test that the WeakKeyDictionary still contains an entry for a certain object
assert dict_with_weak_keys[Object.from_id(ref_to_obj().__id__())] is not None

# Delete the obj and check that it's gone from the WeakKeyDictionary
del ref_to_obj()
assert not dict_with_weak_keys
