fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class TestGetVariableScope(unittest.TestCase):

    def test_getVariableScope(self):
        # Test getVariableScope with default value
        with self.assertRaises(ValueError):
            getVariableScope('test1')
        # Test getVariableScope with keyword arg
        with self.assertRaises(ValueError):
            getVariableScope(test1=1)
        # Test getVariableScope with keyword arg
        with self.assertRaises(ValueError):
            getVariableScope(test1=1, test2=2)
        # Check we get the default value
        self.assertEqual(7, getVariableScope(default=7))
        # Check we get an object declared in the caller's global scope
        self.assertIs(BAR, getVariableScope('BAR'))


class TestGetVariantScope(unittest.TestCase):

    def test_getVariantScope(self):
        # Test getVariableScope with default value
        with self.assertRaises(ValueError):
            getVariantScope('test1')
        # Test get
