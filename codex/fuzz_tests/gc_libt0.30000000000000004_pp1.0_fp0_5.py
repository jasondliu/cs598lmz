import gc, weakref

from . import _test_mixin

class TestWeakRef(_test_mixin.TestWeakRefMixin, unittest.TestCase):
    def _make_weakref(self, obj):
        return weakref.ref(obj)

    def _make_weakref_callback(self, obj):
        return weakref.ref(obj, self._callback)

    def _make_weakref_proxy(self, obj):
        return weakref.proxy(obj)

    def _make_weakref_proxy_callback(self, obj):
        return weakref.proxy(obj, self._callback)

    def _callback(self, obj):
        self.callback_obj = obj

    def _callback_check(self, obj):
        self.assertEqual(self.callback_obj, obj)

    def test_callback(self):
        self.callback_obj = None
        obj = self._make_object()
        ref = self._make_weakref_callback(obj)
        self._callback_check(obj)
        obj = None
        gc.collect()
