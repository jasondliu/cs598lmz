import mmap
import os
import sys
import tempfile
import textwrap
import unittest

import git

from git_autofixup import autofixup, filters
from git_autofixup.testing import assert_git_output


class TestFilters(unittest.TestCase):
    def test_file_contains_line_with_regex(self):
        p = filters.file_contains_line_with_regex('x')
