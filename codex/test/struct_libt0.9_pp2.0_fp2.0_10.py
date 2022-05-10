import _struct
import unittest
import sys
import os

class Format:

    def __init__(self, format, struct_format, skip, test_value):
        self.format = format
        self.struct_format = struct_format
        self.skip = skip
        self.test_value = test_value

    def get_format(self):
        return self.format

    def get_struct_format(self):
        return self.struct_format

    def get_skip(self):
        return self.skip

    def get_value(self):
        return self.test_value

    def __str__(self):
        return str(self.get_struct_format()) + " (" + str(self.get_format(), 'utf-8') + ")"

