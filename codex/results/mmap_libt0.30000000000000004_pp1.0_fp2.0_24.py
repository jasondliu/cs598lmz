import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from . import test_util
from . import util

from . import test_util
from . import util

class TestCase(test_util.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        super(TestCase, self).tearDown()

    def _run_test(self, test_name, args, expected_output,
                  expected_returncode=0, expected_stderr=None,
                  expected_stdout=None, expected_stderr_regex=None,
                  expected_stdout_regex=None):
        """Runs the test, and checks the output and return code."""
        # Create a temp dir to run the test in.
        tempdir = tempfile.mkdtemp()
        try:
            #
