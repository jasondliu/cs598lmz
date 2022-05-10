import mmap
import os
import re
import sys
import subprocess
import tempfile
import time
import unittest

from . import common
from . import util

# The test_* functions in this file are discovered and run by test.py.
# They must have this form, take no arguments, and return nothing.

# pylint: disable=missing-docstring

# The tests in this file are run in a specific order.  The order is
# determined by the name of the test function.  If you add a test,
# please add it at the end of the appropriate section.

def test_00_init():
  common.init_test_env()
  common.setup_test_repos()

def test_01_basic_workflow():
  common.basic_workflow()

def test_02_basic_workflow_with_merge():
  common.basic_workflow_with_merge()

def test_03_basic_workflow_with_branch():
  common.basic_workflow_with_branch()

def test_04_
