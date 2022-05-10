fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class TestFunc(object):
    def test__call_with_args(self):
        def f(a):
            return a
        self.assertEqual(f(1), 1)
        self.assertEqual(f(a=1), 1)
        self.assertEqual(f(1, a=1), 1)
        self.assertRaises(TypeError, f, 1, 2, 3)
        self.assertRaises(TypeError, f, 1, 1, a=1)
        self.assertRaises(TypeError, f, 1, a=1, b=1)

    def test_doc_attr(self):
        self.assertEqual(f.__doc__, "docstring")

    def test_name_attr(self):
        self.assertEqual(f.__name__, "f")

    def test_dict_attr(self):
        self.assertEqual(f.__dict__, {"attr": 1})
        self.assertRaises(TypeError, f.__dict__.clear)

    def
