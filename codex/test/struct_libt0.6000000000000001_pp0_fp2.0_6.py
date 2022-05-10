import _struct
import sys

import pytest

from _testcapi import getargs_keywords_only

from test.support import run_unittest, cpython_only, check_impl_detail


class KeywordOnlyTestCase(unittest.TestCase):

    def test_keyword_only_args(self):
        # Test that keyword-only arguments work.
        self.assertEqual(getargs_keywords_only(1, 2, 3), (1, 2, 3))
        self.assertEqual(getargs_keywords_only(1, 2, x=3), (1, 2, 3))
        self.assertEqual(getargs_keywords_only(1, 2, x=3, y=4), (1, 2, 3))
        self.assertEqual(getargs_keywords_only(1, 2, y=4, x=3), (1, 2, 3))
        self.assertEqual(getargs_keywords_only(1, x=2, y=4, z=6), (1, 2, 4))

