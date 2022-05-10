import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

'''


def test_dealloc_nested(self):
    import _weakref

    class A(object):
        pass

    def callback(x):
        del lst[0]

    keepalive = []
    lst = [str()]
    a = A()
    a.c = a
    keepalive.append(weakref.ref(a, callback))
    del a

    self.assertEqual(len(lst), 1)
    _weakref.proxy(A())
    self.assertEqual(len(lst), 0)


class TestWeakRef(BaseTestChecker):

    def test_constructor(self):
        class Foo(object):
            pass

        f = Foo()
        w = weakref.ref(f)
        self.assertTrue(w() is f)
        self.assertIs(type(w), weakref.ReferenceType)
        self.assertRaises(TypeError, weakref.ref, Foo)
        self.assertRaises(
