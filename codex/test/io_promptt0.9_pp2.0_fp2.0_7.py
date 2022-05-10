import io
# Test io.RawIOBase forwarding
# https://docs.python.org/3/library/stdtypes.html#io.RawIOBase
#
# NOTE: This test case only tests the end-of-file case. We're unable to test
#       other cases because we don't have any other real raw I/O class to
#       instantiate.
import unittest
