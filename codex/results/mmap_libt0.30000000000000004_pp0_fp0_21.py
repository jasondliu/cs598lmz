import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import urllib
import zipfile

from . import config
from . import constants
from . import errors
from . import util
from . import version

# TODO(davidben): This file is a mess. Clean it up.

# The location of the Chromium source root.
_SOURCE_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))

# The location of the Chromium build output directory.
_BUILD_DIR = os.path.join(_SOURCE_ROOT, 'out', 'Release')

# The location of the Chromium build output directory.
_BUILD_DIR_DEBUG = os.path.join(_SOURCE_ROOT, 'out', 'Debug')

# The location of the Chromium build output directory.
_BUILD_DIR_ASAN = os.path.join(_SOURCE_ROOT, 'out', 'Release_asan')
