import lzma
lzma.LZMAFile

import os
import sys
import shutil
import tempfile
import subprocess
import tarfile
import zipfile
import contextlib
import collections

import pytest

from . import util

# The path to the script that should be used for testing.
SCRIPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts', 'xar.py'))

# The path to the test data.
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')

# The path to the test output directory.
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'output')

# The path to the test output directory.
TMP_PATH = os.path.join(os.path.dirname(__file__), 'tmp')

# The path to the test output directory.
TMP2_PATH = os.path.join(os.path.dir
