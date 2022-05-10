fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc string'

class LazyTest(unittest.TestCase):

    def setUp(self):
        self.lazy_fn = lazy(fn)

    def test_lazy_fn_attributes(self):
        self.assertEqual(self.lazy_fn.__name__, 'fn')
        self.assertEqual(self.lazy_fn.__doc__, 'doc string')
        self.assertEqual(self.lazy_fn.__module__, 'test_lazy')

    def test_lazy_fn_evaluation(self):
        self.assertEqual(self.lazy_fn(), None)

    def test_lazy_fn_is_lazy(self):
        self.assertEqual(self.lazy_fn.is_lazy, True)


class LazyClassTest(unittest.TestCase):

    def setUp(self):
        self.lazy_TestClass = lazy(TestClass
