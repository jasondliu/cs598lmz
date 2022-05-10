import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class TestClass(object):

    @staticmethod
    def callback(a, b):
        return a + b

    def test_staticmethod(self):
        fun = FUNTYPE(self.callback)
        assert fun(1, 1) == 2

class TestClass2(object):

    @classmethod
    def callback(cls, a, b):
        return a + b

    def test_classmethod(self):
        fun = FUNTYPE(self.callback)
        assert fun(1, 1) == 2
</code>
As long as the method doesn't use <code>self</code> it can be used in this way.

