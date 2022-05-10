import codecs
# Test codecs.register_error('test', lambda x: ('',x.end))
import io
import pytest
import re
import sys
import warnings
from test import support, test_genericpath

# skip tests if _locale module not available
support.import_module('_locale')

# need to save the original open to call with non-UTF-8 names
_builtin_open = open

# Need to save the original getpreferredencoding to check whether it
# returns None.
_builtin_getpreferredencoding = locale.getpreferredencoding

# Some tests need the user encoding, but they don't work under
# Windows without knowing the code page.
try:
    user_encoding = locale.getdefaultlocale()[1]
except ValueError:
    user_encoding = None

# Skip tests on Windows if we don't know the code page.
if sys.platform == 'win32' and user_encoding is None:
    user_encoding = 'skip_locale_tests'

# save the environment, so we can mess with it
libc_encoding = None
