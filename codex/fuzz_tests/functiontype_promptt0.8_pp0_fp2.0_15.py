import types
# Test types.FunctionType

class FunctionTypeTests(unittest.TestCase):

    def test_types(self):
        self.assertIn(types.FunctionType, types.__all__)

    @unittest.skipUnless(hasattr(types, 'UnboundMethodType'),
                         'types.UnboundMethodType not defined')
    def test_UnboundMethodType(self):
        self.assertIn(types.UnboundMethodType, types.__all__)

    def test_attributes(self):
        def f(): pass
        self.assertIn('__call__', dir(types.FunctionType))
        self.assertIn('__code__', dir(types.FunctionType))
        self.assertIn('__defaults__', dir(types.FunctionType))
        self.assertIn('__get__', dir(types.FunctionType))
        self.assertIn('__globals__', dir(types.FunctionType))
        self.assertIn('__kwdefaults__', dir(types.FunctionType))
        self.assertIn('__name__', dir(types.FunctionType))

