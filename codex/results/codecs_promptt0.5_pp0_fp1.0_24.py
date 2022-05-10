import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

# Test that the default encoding is not "ascii"
# Note: the default encoding is set in site.py
# This is used by the site module to set the site.py
# encoding attribute.
import sys
if sys.getdefaultencoding() == 'ascii':
    raise Exception("sys.getdefaultencoding() should not be 'ascii'")

# Test the default encoding
# This should be UTF-8
# (see http://www.python.org/dev/peps/pep-0263/)
import locale
if locale.getpreferredencoding() != 'UTF-8':
    raise Exception("locale.getpreferredencoding() should be 'UTF-8'")

# Test that the default error handler is not 'strict'
# This is used by the site module to set the site.py
# encoding attribute.
if sys.getdefaultencoding() == 'ascii':
    raise Exception("sys.getdefaultencoding() should not be 'ascii'")

# Test the default error
