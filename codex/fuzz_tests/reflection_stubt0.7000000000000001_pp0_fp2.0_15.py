fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

import sys
if sys.version_info[0] > 2:
    del gi

try:
    del i
except NameError:
    pass

sys.modules['__builtin__'] = sys.modules['builtins']
import __builtin__

import os

import six

from snakeoil.test.mixins import TempDirMixin
from snakeoil.test.test_caching import PyPyMixin
from snakeoil.test import TestCase, SkipTest
from snakeoil.test import mk_cpy_loadable_testcase, mk_cpy_loadable_module_testcase

from snakeoil import compatibility
from snakeoil.osutils import listdir_files, pjoin, abspath, normpath, normjoin
from snakeoil.osutils.deprecated import movefile
from snakeoil.osutils.mount import Tmpfs
from snakeoil.osutils.findfile import find_binary
from snakeoil.osutils.findfile import find_library
from snakeoil.osutils.findfile import find_module
from snakeoil.osutils.findfile
