import _struct
# Test _struct.Struct. _struct can be imported either explicitly or implici
# as part of the _sre module.
import _sre
import sre_compile
import sre_constants
import sre_parse
import sys
import types
import unittest
from unittest import mock
import warnings

class SRE_PatternTest(unittest.TestCase):

    def test_exception(self):
        self.assertEqual(sre_constants.error.pattern,
                         sre_constants.error.__doc__)

    def test_flags(self):
        # sre_parse.Pattern methods
        for method_name in ('getwidth', 'groups', 'groupindex'):
            with self.subTest(method_name=method_name):
                with self.assertRaisesRegex(
                        sre_constants.error,
                        'no current pattern'):
                    getattr(sre_parse.Pattern, method_name)()
        s = sre_parse.Pattern()
        s.flags
        with self.assertRaisesRegex(
                Type
