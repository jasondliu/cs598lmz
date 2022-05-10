import _struct
# Test _struct.Struct
from test import test_support

# Some of the tests will cause a struct.error to be raised, with certain
# error messages.  These messages are specific to the platform, so we need
# to make sure we get the right ones for the platform we're actually
# running the tests on.

if test_support.is_jython:
    # Jython has less-detailed error messages

    expected_error_message = "bad char in struct format"
    expected_error_regexp = r'bad char in struct format'

elif test_support.is_cpython:
    # CPython has more-detailed error messages

    if sys.byteorder == 'little':
        expected_error_message = "bad char in struct format"
    else:
        expected_error_message = "bad char in struct format. format requires a 'little' endian format string"

    expected_error_regexp = r'bad char in struct format. format requires a'

else:
    raise NotImplementedError("test must run on cpython or jython!")



