import weakref
# Test weakref.ref(dict) and weakref.ref(dict.items)
import _weakref

class TestWeakRef:

    def test_basic(self):
        d = {1:1}
        p = weakref.proxy(d)
        assert p[1] == 1
        assert p == {1:1}
        assert repr(p) == repr(d)
        raises(TypeError, p.clear)
        raises(TypeError, p.update, {})
        raises(TypeError, p.__setitem__, 1, 2)
        raises(TypeError, p.__delitem__, 1)
        raises(TypeError, p.setdefault, 1, 2)
        raises(TypeError, p.pop, 1)
        raises(TypeError, p.popitem)
        raises(TypeError, p.__iadd__, {})
        raises(TypeError, p.__imul__, 2)
        raises(TypeError, p.clear)
        raises(TypeError, p.update, {})
        raises(TypeError, p.__setitem__, 1
