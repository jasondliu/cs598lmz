fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class Mi(object):
    @property
    def __code__(self):
        return None


fi = Mi()


class TestFunctionType(unittest.TestCase):
    def test_simple(self):
        self.assertIn(
            'function',
            type(fn).__repr__(),
        )

    def test_code(self):
        self.assertRaises(
            TypeError,
            getattr,
            fi,
            '__code__',
        )


if __name__ == "__main__":
    unittest.main()
