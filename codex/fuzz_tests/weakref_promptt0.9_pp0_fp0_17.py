import weakref
# Test weakref.ref on builtin, function and type
def testWeakRefWithBuiltin():
    o = object
    r1 = weakref.ref(o)
    check(r1().__class__ is object)


def testWeakRefWithFunction():
    def f():
        return 5

    r2 = weakref.ref(f)
    check(r2(
    )() == 5)


def testWeakRefWithType():
    class C(object):
        pass

    r3 = weakref.ref(C)
    check(r3().__class__ is C)


check(weakref.WeakKeyDictionary is weakref.WeakKeyDictionary)

# Check that the class has a new attribute called "__doc__"
check(weakref.WeakKeyDictionary.__doc__ == weakref.WeakKeyDictionary.__doc__)

# Check that the class has a new attribute called "weakrefs_key"
check(weakref.WeakKeyDictionary.weakrefs_key is weakref.WeakKeyDictionary.weakrefs_key)

# Check that the class
