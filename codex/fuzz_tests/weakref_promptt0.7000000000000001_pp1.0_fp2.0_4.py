import weakref
# Test weakref.ref() on builtin type instances

def test_ref(instance):
    print(repr(weakref.ref(instance)))


class C(object):
    pass


def main():
    test_ref(C)
    test_ref(C())
    test_ref(str)
    test_ref('abc')
    test_ref(int)
    test_ref(1)
    test_ref(type)
    test_ref(object)
    test_ref(type(None))
    test_ref(bool)
    test_ref(True)
    test_ref(False)
    test_ref(float)
    test_ref(1.0)
    test_ref(complex)
    test_ref(1.0 + 0.0j)


main()
