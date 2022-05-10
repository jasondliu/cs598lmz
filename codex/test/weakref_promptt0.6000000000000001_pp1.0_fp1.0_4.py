import weakref
# Test weakref.ref(instance)
# Test weakref.ref(class)
# Test weakref.ref(None)
# Test weakref.ref(True)
# Test weakref.ref(False)
# Test weakref.ref(10)
# Test weakref.ref(10.0)
# Test weakref.ref(10.0+0.0j)
# Test weakref.ref('abc')
# Test weakref.ref(b'abc')
# Test weakref.ref(bytearray(b'abc'))
# Test weakref.ref(b'abc', self.ref_callback)


class TestWeakref(unittest.TestCase):

    def setUp(self):
        self.called = False
        self.callback_called = False

    def ref_callback(self, ref):
        self.callback_called = True

    def test_ref(self):
        obj = object()
        ref = weakref.ref(obj)
        self.called = False

        def callback(arg):
            self.called = True
