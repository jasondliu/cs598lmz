import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import unittest

import pytest

from . import test_common

def _get_test_dir():
    return os.path.dirname(os.path.abspath(__file__))

def _get_test_data_dir():
    return os.path.join(_get_test_dir(), 'test_data')

def _get_test_data_file(filename):
    return os.path.join(_get_test_data_dir(), filename)

def _get_test_script_dir():
    return os.path.join(_get_test_dir(), 'test_scripts')

def _get_test_script_file(filename):
    return os.path.join(_get_test_script_dir(), filename)

def _get_test_src_dir():
    return os.path.join(_get_test_dir(), '..', 'src')

def _get_test_src_file(filename):
