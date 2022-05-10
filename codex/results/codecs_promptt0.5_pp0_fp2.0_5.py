import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

import re
import os
import sys
import time
import array
import struct
import math
import pickle
import socket
import random
import subprocess

# Test using and importing the _winreg module
try:
    import _winreg
except ImportError:
    _winreg = None

import _collections
import test.test_support
import unittest
import warnings
import gc
import weakref

from test import mapping_tests
from test import string_tests
from test import test_support

# Silence Py3k warning
if sys.py3kwarning:
    warnings.filterwarnings("ignore", ".*builtin .* is deprecated
