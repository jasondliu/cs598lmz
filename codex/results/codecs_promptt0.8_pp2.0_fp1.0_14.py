import codecs
# Test codecs.register_error()
import platform
from test import test_support
try:
    import locale
except ImportError:
    locale = None

# Note: for now, this only tests the interface, there are no failing tests

TPASS = test_support.TestFailed
TFAIL = test_support.TestFailed

def _get_string_encoding():
    encoding = sys.getdefaultencoding()
    # sys.getdefaultencoding() may return "ascii" even if the filesystem
    # encoding is not "ascii".  This happens if sitecustomize.py exists and
    # does a "sys.setdefaultencoding('ascii')".  We need to check
    # sys.getfilesystemencoding() which never returns "ascii".
    if encoding == "ascii":
        encoding = sys.getfilesystemencoding()
    return encoding

# On Windows, test_importlib is run with the locale encoding explicitly
# set to "ascii".  First, that is the default encoding for Python 3.  But
# second, it means we can check for the
