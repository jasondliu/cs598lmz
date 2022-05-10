gi = (i for i in ())
# Test gi.gi_code.co_filename

import sys

# Ensure that the module object of a compiled module has the correct
# __file__ attribute.

mod = __import__('sys')
if not mod.__file__.endswith('sys.pyc') and not mod.__file__.endswith('sys.pyo'):
    print('__file__ wrong:', mod.__file__)

# Ensure that a compiled module has the correct __file__ attribute.

from sys import version_info
if not version_info.__file__.endswith('sys.pyc') and not version_info.__file__.endswith('sys.pyo'):
    print('__file__ wrong:', version_info.__file__)

# Ensure that an extension module has the correct __file__ attribute.

import _testcapi
if not _testcapi.__file__.endswith('_testcapi.so'):
    print('__file__ wrong:', _testcapi.__file__)

# Ensure that the module object of a frozen module has the correct
