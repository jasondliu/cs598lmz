import types
# Test types.FunctionType

class TestTypesFunctionType(unittest.TestCase):

    def test_types_FunctionType(self):
        self.assertEqual(types.FunctionType.__module__, 'types')
        self.assertTrue(type(types.FunctionType) is type)
        self.assertEqual(types.FunctionType.__doc__,
"""function(code, globals[, name[, argdefs[, closure]]])

Create a function object from a code object and a dictionary.
The optional name string overrides the name from the code object.
The optional argdefs tuple specifies the default argument values.
The optional closure tuple supplies the bindings for free variables.""")
        self.assertEqual(types.FunctionType.__name__,
                         'function')

    def test_types_FunctionType_call(self):
        self.assertRaises(TypeError, types.FunctionType)
        self.assertRaises(TypeError, types.FunctionType, None)
        self.assertRaises(TypeError, types.FunctionType, None, None)
        self.assertRaises(Type
