import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from . import util

def _get_test_dir():
    return os.path.dirname(os.path.realpath(__file__))

def _get_test_data_dir():
    return os.path.join(_get_test_dir(), 'data')

def _get_test_data_path(name):
    return os.path.join(_get_test_data_dir(), name)

def _get_test_tmp_dir():
    return os.path.join(_get_test_dir(), 'tmp')

def _get_test_tmp_path(name):
    return os.path.join(_get_test_tmp_dir(), name)

def _get_test_script_path(name):
    return os.path.join(_get_test_dir(), 'scripts', name)

def _get_test_script_dir():
    return os.path.join(_get_test_dir(), 'scripts
