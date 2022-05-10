import weakref
# Test weakref.ref(n) for a variety of values for n.

def check(ob):
    r = weakref.ref(ob)
    if ob:
        # object exists
        if r() is None:
            raise ValueError("Object exists but returned None")
        if r() is not ob:
            raise ValueError("Object exists but returned another object")
    else:
        # object doesn't exist
        if r() is not None:
            raise ValueError("Object doesn't exist but didn't return None")

class C:
    pass

