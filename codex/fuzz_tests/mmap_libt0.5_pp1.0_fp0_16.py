import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile

from distutils import sysconfig
from distutils.command.build_ext import build_ext
from distutils.errors import (CCompilerError, DistutilsExecError,
                              DistutilsPlatformError)
from distutils.version import LooseVersion

# This is the only place where we depend on the Python version.
# We can't use the 'six' module because it is not available in
# the bootstrap process.
if sys.version_info < (2, 6):
    raise RuntimeError('This package requires Python 2.6 or newer')

# The following code is copied from the 'six' module.
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes
else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type
