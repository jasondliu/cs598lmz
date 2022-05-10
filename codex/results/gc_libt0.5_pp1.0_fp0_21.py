import gc, weakref
import numpy as np

class TestWeakref():
    def test_weakref_to_object(self):
        # issue #20
        import weakref
        class Test(object):
            def __init__(self, value):
                self.value = value
        t = Test(10)
        assert t.value == 10
        w = weakref.ref(t)
        assert w().value == 10
        t.value = 20
        assert w().value == 20
        del t
        gc.collect()
        assert w() is None

    def test_weakref_to_object_with_finalizer(self):
        import weakref
        class Test(object):
            def __init__(self, value):
                self.value = value
            def __del__(self):
                pass
        t = Test(10)
        assert t.value == 10
        w = weakref.ref(t)
        assert w().value == 10
        t.value = 20
        assert w().value == 20
        del t
        gc.collect()
       
