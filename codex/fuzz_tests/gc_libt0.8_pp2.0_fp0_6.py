import gc, weakref

import pytest

from .. import weak_method_proxy as wmp

GC_TRESHOLD = 3
 
def test_weak_method_proxy():
    class A(object):
        def __init__(self):
            self.ident = 'A'
            self.meth_called = 0
        def meth(self):
            self.meth_called += 1
            return self.ident
 
    a = A()
    wm = wmp.WeakMethodProxy(a.meth)
    assert wm() == 'A'
    assert a.meth_called == 1
    del a
    for i in range(GC_TRESHOLD + 1):
        if i < GC_TRESHOLD:
            assert wm() == 'A'
            assert gc.is_tracked(wm)
        else:
            with pytest.raises(wmp.ReferenceError):
                wm()
            assert gc.get_referrers(wm)
            assert not gc.is_tracked(wm)
    assert 'wm' not
