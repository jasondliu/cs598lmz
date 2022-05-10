import codecs
# Test codecs.register_error('ignore')
#
# This tests handles the cases where the error handler accepts a string
# argument only, or a unicode argument only.

import codecs
import sys
import unittest

class MockUnicodeEncodeError(Exception):
    def __init__(self, obj, *args):
        self.object = obj
        Exception.__init__(self, *args)
    def __str__(self):
        return Exception.__str__(self) + ": " + repr(self.object)

class MockUnicodeDecodeError(Exception):
    def __init__(self, obj, *args):
        self.object = obj
        Exception.__init__(self, *args)
    def __str__(self):
        return Exception.__str__(self) + ": " + repr(self.object)

class MockUnicodeTranslateError(Exception):
    def __init__(self, obj, *args):
        self.object = obj
        Exception.__init__(self, *args)
