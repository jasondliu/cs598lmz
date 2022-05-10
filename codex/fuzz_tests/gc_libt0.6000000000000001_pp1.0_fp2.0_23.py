import gc, weakref

class TestGC(unittest.TestCase):
    def test_gc(self):
        class C(object):
            pass
        class D(object):
            pass
        class E(object):
            pass
        class F(object):
            pass
        class G(object):
            pass

        obj = C()
        obj.x = D()
        obj.x.y = obj
        obj.x.y.z = E()
        obj.x.y.z.x = obj.x
        obj.x.y.z.x.y = obj.x.y.z

        del obj.x.y.z.x.y

        obj.x.y.z.x.y = F()
        obj.x.y.z.x.y.z = obj.x.y.z

        del obj.x.y.z.x
        del obj.x.y.z
        del obj.x.y
        del obj.x

        obj.x = G()
        obj.x.y = obj
        obj.x.
