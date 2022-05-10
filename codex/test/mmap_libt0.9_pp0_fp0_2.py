import mmap
import os
import pickle
import subprocess
import re
import shutil
import struct
import sys
import tempfile
import unittest
import zipfile

if sys.platform == 'win32':
    from ctypes import windll

import pkg_resources

import pytest
import pytest_cov

from coverage.backward import bytes_to_int, collect_callers, itervalues, pairs  # NOQA

PY3 = (sys.version_info[0] >= 3)

if PY3:
    func_attrs = {'__code__': 'co_code', '__defaults__': 'co_defaults'}
else:
    func_attrs = {'func_code': 'co_code', 'func_defaults': 'co_defaults'}

# This is the runtime compiled bytecode for this function.
def_code = compile("def f(): a = 1; b = 2; c = a+b", "<test>", "exec")


