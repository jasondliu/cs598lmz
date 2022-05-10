gi = (i for i in ())
# Test gi.gi_code.co_filename is not None.

# This test case is a test for a bug in the PyEval_EvalFrameEx function.
# The bug was that the value of the 'f_lineno' member of a frame was not
# updated when 'f_trace' was set to a non-NULL value.  This caused
# debugging functions (e.g. trace_dispatch) to fail since the line number
# was always reported as 1.

import sys
import types
import unittest

class TraceTestCase(unittest.TestCase):

    def test_lineno(self):
        frame_lineno = [None]
        def get_line(frame, event, arg):
            frame_lineno[0] = frame.f_lineno
            return get_line

        sys.settrace(get_line)
        from test.badsyntax_future3 import x
        assert frame_lineno[0] == 3, frame_lineno[0]
        sys.settrace(None)
        x = 4

def test_main():
    test_support.
