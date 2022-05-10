import codecs
# Test codecs.register_error
import sys
import unittest
from test import test_support

# The tests in this file are intended to exercise the error handling
# code in the Python codecs module.  Each test is a class derived from
# the TestBase class defined below.  The test classes are instantiated
# in the 'suite()' function, and the suite is run by the standard
# regrtest.py script.

# The codecs module defines a number of standard error handlers, which
# are listed in the 'error_handlers' dictionary below.  Each test class
# is defined for a given error handler.  The 'encoding' and 'errors'
# attributes of the test class are set to the encoding and error handler
# for that test class.

error_handlers = {
    'strict': codecs.strict_errors,
    'ignore': codecs.ignore_errors,
    'replace': codecs.replace_errors,
    'xmlcharrefreplace': codecs.xmlcharrefreplace_errors,
    'backslashreplace': codecs.backslashreplace_errors,
}


