import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.c.c)
keepali0e.append(a.c.c.c)
keepali0e.append(a.c.c.c.c)
a.c.c.c.c.c=lst
del keepali0e
del a
del lst
assert_raises(RuntimeError,gc.collect)

class TestWeakrefModule(unittest.TestCase):

    def test_ref(self):
        o = TestWeakrefModule
        p = weakref.ref(o)
        q = weakref.ref(o)
        r = weakref.ref(o)
        self.assertEqual(p(), o)
        self.assertEqual(q(), o)
        self.assertEqual(r(), o)
        self.assertIs(p(), q())
        self.assertIs(p(), r())
        self.assertIs(p(), o)
        self.assertIs(q(), r
