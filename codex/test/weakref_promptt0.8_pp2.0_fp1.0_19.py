import weakref
# Test weakref.ref
try:
    weakref.ref
except AttributeError:
    raise ImportError("your platform's weakref module doesn't define ref")

def trivial_callback(reference, self):
    self.referenced = reference

class BasicRefTestCase(unittest.TestCase):
    def setUp(self):
        self.ob = object()
        self.ref = weakref.ref(self.ob)
        self.callback_result = []
        self.ref_callback = weakref.ref(self.callback_result,
                                        trivial_callback)

    def callback(self, result):
        self.callback_result.append(result)

    def test_callable(self):
        # Test callability
        self.ref()

    def test_hashable(self):
        hash(self.ref)

    def test_equality(self):
        self.assertEqual(self.ref, weakref.ref(self.ob))
        self.assertEqual(self.ref_callback, weakref.ref(self.callback_result))
        self.assertNot
