gi = (i for i in ())
# Test gi.gi_code is a code object
test.test(isinstance(gi.gi_code, types.CodeType))
# Test gi.gi_frame is a frame object
test.test(isinstance(gi.gi_frame, types.FrameType))

# Test sys.exc_info()
try:
    raise ValueError
except:
    exc_info = sys.exc_info()
    test.test(exc_info[0] == ValueError)
    # Test the traceback is an instance of the TracebackType
    test.test(isinstance(exc_info[2], types.TracebackType))

# Test sys.exc_clear()
try:
    raise ValueError
except:
    exc_info = sys.exc_info()
    test.test(exc_info[0] == ValueError)
    # Test sys.exc_clear()
    sys.exc_clear()
    # Test sys.exc_info() after exc_clear()
    test.test(sys.exc_info() == (None, None, None))

# Test sys.exc_traceback
def
