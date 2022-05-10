import types
# Test types.FunctionType and types.BuiltinFunctionType
class TypeTest(unittest.TestCase):
    def test_types(self):
        self.assertIsInstance(all, types.BuiltinFunctionType)
        self.assertIsInstance(all, types.FunctionType)


if __name__ == "__main__":
    unittest.main()
