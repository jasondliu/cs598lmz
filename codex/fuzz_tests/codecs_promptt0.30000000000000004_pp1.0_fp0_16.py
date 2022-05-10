import codecs
# Test codecs.register_error()

# This test is not exhaustive, but it should catch most of the bugs.

import codecs
import sys

# Test the strict error handler

def test_strict(encoding, input, expected_output):
    # Encode
    output = codecs.encode(input, encoding, 'strict')
    if output != expected_output:
        print('%s.encode("strict") failed:' % encoding)
        print('    Input:', repr(input))
        print('    Expected output:', repr(expected_output))
        print('    Actual output:', repr(output))
        print('    Error:', sys.exc_info()[1])
        raise TestFailed

    # Decode
    output = codecs.decode(expected_output, encoding, 'strict')
    if output != input:
        print('%s.decode("strict") failed:' % encoding)
        print('    Input:', repr(expected_output))
        print('    Expected output:', repr(input))
        print('    Actual output:', repr(
