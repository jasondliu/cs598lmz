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


test_invalid_object()
print("Testing finalizing objects that are not hashable...")
not_hashable = [NotHashable(), C(), D()]
alive = weakref.WeakKeyDictionary()
trash = []


def callback(object):
    trash.append(object)


#    print "Callback received object:", object
for o in not_hashable:
    alive[o] = 1


