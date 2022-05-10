import types
# Test types.FunctionType
class FunctionTypeTestCase(unittest.TestCase):
    def test_types(self):
        self.assertEqual(True, isinstance(FunctionTypeTestCase.test_types, types.FunctionType))
        self.assertEqual(True, isinstance(lambda x: x, types.FunctionType))
        self.assertEqual(False, isinstance(1, types.FunctionType))
        
        it = iter(range(5))
        self.assertEqual(True, isinstance(it.__next__, types.FunctionType))
        self.assertEqual(False, isinstance((x for x in range(5)), types.FunctionType))
    
    def test_callable(self):
        self.assertEqual(True, callable(FunctionTypeTestCase.test_callable))
        self.assertEqual(True, callable(lambda x: x))
        
        it = iter(range(5))
        self.assertEqual(True, callable(it.__next__))
        
        self.assertEqual(False, callable(1
