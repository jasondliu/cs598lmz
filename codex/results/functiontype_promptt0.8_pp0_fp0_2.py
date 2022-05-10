import types
# Test types.FunctionType, but no Test_types since the tests are
# all here in types_tests.py

class TypesTestCase(unittest.TestCase):

    def test_truth_values(self):
        self.assertTrue(bool(types.BuiltinFunctionType))
        self.assertTrue(bool(types.BuiltinMethodType))
        self.assertTrue(bool(types.FunctionType))
        self.assertTrue(bool(types.MethodType))
        self.assertTrue(bool(types.GeneratorType))
        self.assertTrue(bool(types.TracebackType))
        self.assertTrue(bool(types.FrameType))
        self.assertTrue(bool(types.CodeType))
        self.assertTrue(bool(types.SimpleNamespace))

    def test_issubclass(self):
        class C: pass
        class D: pass
        class E(C, D): pass
        self.assertIsSubclass(E, C)
        self.assertIsSubclass(E, D)
        self.assertIsNotSubclass(C, E)
        self
