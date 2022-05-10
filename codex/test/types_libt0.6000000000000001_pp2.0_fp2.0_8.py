import types
types.FunctionType = FunctionType
types.MethodType = MethodType
types.BuiltinMethodType = BuiltinMethodType
types.BuiltinFunctionType = BuiltinFunctionType

import sys
sys.setrecursionlimit(100000)

import unittest

from javaproperties import *

class TestJavaproperties(unittest.TestCase):

    def test_load_file(self):
        properties = Properties()
        properties.load(open("test/data/test.properties"))

        self.assertEqual("value", properties["key"])
        self.assertEqual("value", properties["key-with-spaces"])
        self.assertEqual("value", properties["key-with-equals"])
        self.assertEqual("value", properties["key-with-colon"])
