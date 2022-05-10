import weakref
# Test weakref.ref() for referents that are not hashable.
import gc


class NotHashable:
    pass


class C(NotHashable):
    pass


class D(NotHashable):
    pass


def ref(o):
    r = weakref.ref(o)
    print(type(r), r, r())
    return r


def test_invalid_object():
    for o in [NotHashable(), C(), D()]:
        try:
            ref(o)
        except TypeError:
            pass
        else:
            raise TypeError("Should have raised TypeError")
    else:
        print("All OK")


