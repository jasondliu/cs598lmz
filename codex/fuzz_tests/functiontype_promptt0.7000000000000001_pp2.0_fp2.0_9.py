import types
# Test types.FunctionType, types.MethodType, types.BuiltinFunctionType, and types.BuiltinMethodType
import unittest

class TypesTestCase(unittest.TestCase):

    def test_types(self):
        # Check that the three types are separate objects.
        self.assertNotEqual(types.FunctionType, types.MethodType)
        self.assertNotEqual(types.FunctionType, types.BuiltinFunctionType)
        self.assertNotEqual(types.MethodType, types.BuiltinFunctionType)

        # Check that the three types are different from their name.
        self.assertNotEqual(types.FunctionType, 'FunctionType')
        self.assertNotEqual(types.MethodType, 'MethodType')
        self.assertNotEqual(types.BuiltinFunctionType, 'BuiltinFunctionType')
        self.assertNotEqual(types.BuiltinMethodType, 'BuiltinMethodType')

        # Check that the types are what they claim to be by
        # creating an object of each type and testing its type.
        self.assertEqual(type(min),
