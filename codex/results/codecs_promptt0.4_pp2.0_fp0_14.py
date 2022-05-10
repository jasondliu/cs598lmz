import codecs
# Test codecs.register_error()
import sys
import unittest
from test import support
import re

class CodecsModuleTest(unittest.TestCase):

    def test_bug_83495(self):
        # Make sure that we don't raise a SystemError when trying to
        # instantiate an encoder or decoder for an invalid search function
        self.assertRaises(TypeError, codecs.getencoder, 'xxx')
        self.assertRaises(TypeError, codecs.getdecoder, 'xxx')

    def test_bug_83561(self):
        # Make sure that we don't raise a SystemError when trying to
        # instantiate an IncrementalEncoder or IncrementalDecoder for an
        # invalid constructor
        self.assertRaises(TypeError, codecs.getincrementalencoder, 'xxx')
        self.assertRaises(TypeError, codecs.getincrementaldecoder, 'xxx')

    def test_bug_83564(self):
        # Make sure that we don't raise a SystemError when trying to
        # instantiate a StreamWriter or
