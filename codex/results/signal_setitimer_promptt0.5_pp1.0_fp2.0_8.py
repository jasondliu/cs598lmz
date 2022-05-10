import signal
# Test signal.setitimer() with a signal handler that sleeps.

from test.support import verbose, run_with_tz, run_with_locale
from test.support.script_helper import assert_python_ok

# The test is skipped if the timer resolution is too coarse.
# The test is not reliable on Windows, and it is skipped.
@unittest.skipUnless(signal.setitimer(signal.ITIMER_REAL, 0, 0)[0],
                     "timer resolution too coarse")
@unittest.skipIf(sys.platform == "win32",
                 "test not reliable on Windows")
def test_setitimer_signal_handler_sleep():
    if verbose:
        print('\nTesting signal.setitimer() with a signal handler that sleeps')

    # Create a subprocess that runs the following code:
    #     def handler(signum, frame):
    #         time.sleep(2)
    #     signal.signal(signal.SIGALRM, handler)
    #     signal.setitimer(signal.ITIMER_REAL
