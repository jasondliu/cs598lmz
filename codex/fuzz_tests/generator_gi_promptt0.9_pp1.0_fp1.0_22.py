gi = (i for i in ())
# Test gi.gi_code
if i.gi_code:
    raise TestFailed("""\
gi.gi_code should have been None.
*** Warning -- the following result is implementation-dependent! ***
*** This SHOULD be False (CPython) or not exist (Jython) ***
default: {0}""".format(i.gi_code))

# Test gi.gi_frame
if i.gi_frame:
    raise TestFailed("""\
gi.gi_frame should have been null.
*** Warning -- the following result is implementation-dependent! ***
*** This SHOULD be None (CPython) or not exist (Jython) ***
default: {0}""".format(i.gi_frame))

# Test gi.gi_running
if not i.gi_running:
    raise TestFailed("""\
gi.gi_running should have been True.
*** Warning -- the following result is implementation-dependent! ***
*** This SHOULD exist (CPython) or not exist (Jython) ***
default: {0}""".format(i.gi_running))

# Test gi.__reduce
