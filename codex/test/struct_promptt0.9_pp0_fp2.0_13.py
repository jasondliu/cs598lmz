import _struct
# Test _struct.Struct and _struct.error
import unittest
import warnings

class StructTest(unittest.TestCase):
    def test_format(self):
        _struct.Struct('ab')
        _struct.Struct('c')
        _struct.Struct('cb')
        _struct.Struct('cx')
        _struct.Struct('cxcb')
        _struct.Struct('cbxcb')
        _struct.Struct('cbh')
        _struct.Struct('2cbh')
        _struct.Struct('cb9c')
        _struct.Struct('0cb')
    #    _struct.Struct('xb')

        self.assertRaises(TypeError, _struct.Struct, '')
        self.assertRaises(TypeError, _struct.Struct, '(')
        self.assertRaises(TypeError, _struct.Struct, 'a')
        self.assertRaises(TypeError, _struct.Struct, '=b')
        self.assertRaises(TypeError, _struct.Struct, '+b')
