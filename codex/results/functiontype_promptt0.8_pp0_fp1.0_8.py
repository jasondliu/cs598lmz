import types
# Test types.FunctionType and types.LambdaType
import unittest
from unittest.mock import call, mock_open, patch

import coverage
from coverage import env

from tests.coveragetest import CoverageTest
from tests.helpers import TestData
from tests.gold import data_dir


def f1(x):                      # pragma: nested
    """Testing function."""
    return x + 1


class Tests(CoverageTest):
    """Tests of the .__init__.py file."""

    def setUp(self):
        super(Tests, self).setUp()

        # Parent class saves and restores sys.path, we can just modify it.
        sys.path.append(self.nice_file(self.nice_file(self.tmp_dir, 'a'), 'b'))
        sys.path.append(self.nice_file(self.nice_file(self.tmp_dir, 'c'), 'd'))

    def test_version(self):
        # __version__ is right.
        self.assertEqual(coverage.version, env
