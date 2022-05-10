import gc, weakref

try:
    from .base import CachedType
except (ImportError, ValueError):
    from base import CachedType

class gcTest:
    pass

def check(obj):
    assert isinstance(obj, gcTest)
    return obj

class Cached(CachedType):

    def __init__(self):
        CachedType.__init__(self, check)
        self.value = gcTest()

    def getweakref(self):
        return weakref.ref(gcTest())


class TestGC:

    def test_instance(self):
        c = Cached()
        assert c.value is c.value

        wr = c.getweakref()
        assert wr() is None

    def test_new(self):
        c = Cached()
        assert c.value is c.value
        c.new()
        assert c.value is not c.value
        assert c.value is c.value

    def test_getweakref(self):
        c = Cached()
        wr = c.getweakref
