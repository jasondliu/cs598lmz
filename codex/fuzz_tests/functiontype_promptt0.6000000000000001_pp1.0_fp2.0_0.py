import types
# Test types.FunctionType()
class FunctionTypeTest(unittest.TestCase):
    def test_FunctionType(self):
        self.assertEqual(types.FunctionType.__module__, 'types')
        self.assertEqual(types.FunctionType.__name__, 'function')

    def test_FunctionType_positive(self):
        self.assertTrue(isinstance(lambda x: x, types.FunctionType))
        self.assertTrue(isinstance(FunctionTypeTest, types.FunctionType))

    def test_FunctionType_negative(self):
        self.assertFalse(isinstance(True, types.FunctionType))
        self.assertFalse(isinstance(12, types.FunctionType))
        self.assertFalse(isinstance('abc', types.FunctionType))
        self.assertFalse(isinstance(b'abc', types.FunctionType))
        self.assertFalse(isinstance(None, types.FunctionType))
        self.assertFalse(isinstance(object(), types.FunctionType))

if __name__ == '__main__':
    unittest.main()
