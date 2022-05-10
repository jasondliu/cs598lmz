import types
types.FunctionType = types.BuiltinFunctionType

import os
import sys
import math
import unittest

import arcpy

class TestDataTypeInteger(unittest.TestCase):
    '''Test Integer data type.'''
    def setUp(self):
        self.field_name = "test_int"
        self.field_precision = 2
        self.field_scale = 0
        self.field_length = 10
        self.field_alias = "Test Integer"
        self.field_is_nullable = True
        self.field_is_required = False
        self.field_domain = ""

        self.field = arcpy.Field()
        self.field.name = self.field_name
        self.field.type = "Integer"
        self.field.precision = self.field_precision
        self.field.scale = self.field_scale
        self.field.length = self.field_length
        self.field.aliasName = self.field_alias
        self.field.isNullable = self.field_is_nullable
