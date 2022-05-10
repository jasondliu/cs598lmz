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

for x in (None,
          [],
          [1,2,3],
          (),
          (1,2,3),
          "",
          "foo",
          1,
          1.0,
          1L,
          C()):
    check(x)

# Check that weakrefs to old-style instances work, including weakrefs
# to instances of classes derived from built-in types.  SF bug #606580
class I:
    pass

i = I()
r = weakref.ref(i)
