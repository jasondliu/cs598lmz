import ctypes
# Test ctypes.CField structure in opcodes.h

import unittest
from test import support


class CFieldTest(unittest.TestCase):
    def check_field(self, field, name, length, offset, type_,
                    is_signed = False):
        self.assertEqual(field.name, name)
        self.assertEqual(field.length, length)
        self.assertEqual(field.offset, offset)
        self.assertEqual(field.type, type_)
        self.assertEqual(field.is_signed, is_signed)

    def check_fields(self, fields, check_fields):
        for i, check_field in enumerate(check_fields):
            field = fields[i]
            self.check_field(field, *check_field)

    def test_short_oparg(self):
        self.check_fields(ctypes.CField.short_oparg_fields, [
            ('opcode', 2, 0, ctypes.c_ushort, False),
            ('oparg', 6, 2, ctypes.c
