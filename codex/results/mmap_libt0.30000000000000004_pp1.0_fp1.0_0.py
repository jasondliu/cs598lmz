import mmap
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

import test_env  # pylint: disable=W0611,W0403

from v8_suppressions import *  # pylint: disable=W0401,W0614
from v8_suppressions import _GetPlatformSpecificSuppression

import v8_types  # pylint: disable=W0611,W0403

from supressions_util import *  # pylint: disable=W0401,W0614

# Path constants. (Many are relative to the build directory.)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.dirname(os.path.dirname(THIS_DIR))

# The directory containing the test data.
TEST_DATA_DIR = os.path.join(THIS_DIR, 'test_data')

# The directory containing the tools.
TOOLS_DIR = os.path.join(BUILD
