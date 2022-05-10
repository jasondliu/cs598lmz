import codecs
# Test codecs.register_error()
import os
# Test os.path.normcase(path) and os.path.normpath(path)
import sys
# Test sys.getdefaultencoding()
import tempfile
# Test tempfile.TemporaryFile()
import unittest
import warnings

# We have to catch the warnings filters manipulation warnings even if the -W
# option is not given to regrtest.py, because some tests import the warnings
# module and expect that they won't be caught by the default catch_warnings
# context.
warnings.simplefilter('ignore', ResourceWarning)

# unittest.mock is not available in 2.7 (though unittest.mock is available
# for Python 2.7 on PyPI).
try:
    import unittest.mock as mock
except ImportError:
    import mock


def strip_python_stderr(stderr):
    """Strip the stderr of a Python process from potential debug output
    emitted by the interpreter.

    This will typically be run on the result of the communicate() method
    of a subprocess.Popen object
