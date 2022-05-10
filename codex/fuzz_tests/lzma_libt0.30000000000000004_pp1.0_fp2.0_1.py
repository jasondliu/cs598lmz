import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import unittest

import pytest

import pytest_check as check

from . import util

# This is the path to the test data directory.
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# This is the path to the test output directory.
TEST_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')

# This is the path to the test script directory.
TEST_SCRIPT_DIR = os.path.join(os.path.dirname(__file__), 'scripts')


class TestCase(unittest.TestCase):
    """
    Base class for test cases.
    """

    def setUp(self):
        """
        Called before each test method.
        """
        # Create a temporary directory.
        self.temp_dir = tempfile.mkdtemp()

    def tear
