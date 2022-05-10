import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from buildscripts.resmokelib import core
from buildscripts.resmokelib import testing
from buildscripts.resmokelib import utils
from buildscripts.resmokelib.suitesconfig import create_suite_from_config
from buildscripts.resmokelib.testing import interface, testcases
from buildscripts.util import globstar
from buildscripts.util import registry
from buildscripts.util.log import Logger

LOGGER = Logger(__name__)

# This must be kept in sync with the Paths interface in resmokelib/testing/testcases.py.
_TEST_EXECUTOR_FILE = "test_executor.py"
_TEST_EXECUTOR_FILE_ABS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       _TEST_EXECUTOR_FILE)
_TEST_EXECUTOR_FILE_
