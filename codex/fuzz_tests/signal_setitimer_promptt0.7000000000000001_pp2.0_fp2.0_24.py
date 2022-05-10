import signal
# Test signal.setitimer(0, 0).
# The original testcase was:
#   import signal
#   signal.setitimer(0,0)

# This may fail if the system doesn't support setitimer
# (this test is skipped on systems without setitimer support)
try:
    signal.setitimer(0, 0.1)
except (IOError, ValueError):
    raise unittest.SkipTest("system does not support setitimer")

if sys.platform == 'darwin':
    # Issue #19918: test *cannot* be skipped on darwin
    # because it is a requirement for the test_time test
    # suite to work properly (see #19918).
    # On OSX 10.8, setitimer(0, 0) raises OSError:
    #    [Errno 22] Invalid argument.
    # This is a known issue.
    try:
        signal.setitimer(0, 0)
    except OSError as err:
        if err.errno != 22:
            raise

# The following are the tests that
