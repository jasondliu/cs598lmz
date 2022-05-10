import weakref
# Test weakref.ref() constructor for non-callable objects.
class C:
    pass

for obj in [None, 1, 'a', 1.2, [], (), {}]:
    try:
        ref = weakref.ref(obj)
    except TypeError:
        pass
