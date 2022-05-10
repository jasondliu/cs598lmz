import mmap
import os
import re
import sys
import tempfile
import textwrap
import unittest

from six.moves import builtins

try:
    from unittest import mock
except ImportError:
    import mock

import modernize

from modernize.errors import ASTError
from modernize.fixes import fix_six_division

from lib2to3.fixer_base import BaseFix
from lib2to3.pytree import Leaf, Node
from lib2to3.tests.support import Lib2to3TestCase, skip_if_python2

from pycodestyle import BaseReport, Checker

from tests.test_fixes.test_fix_tuple_params import FixTupleParamsTest


class FixAddMissingSelfTest(FixTupleParamsTest):
    fixer = 'add_missing_self'

    def test_add_missing_self(self):
        self.check("""
        class C(object):
            def __init__(x):
                pass
        """, """
        class C(object):
            def __init__(self
