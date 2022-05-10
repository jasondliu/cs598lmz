import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 0.001)

import time

from . import _utils


def main():
    """Main function."""
    _utils.print_header()
    # pylint: disable=bad-continuation
    _utils.print_info("""
This test is not a real test.
It just shows how to use the Python signal module to catch the SIGALRM
signal and run a function every time the signal is emitted.

This is useful, for example, to run a function every X seconds.

In this example we use the signal.setitimer() function to set the
real time interval timer to 0.001 seconds.

The function we run every time the signal is emitted is the print_time()
function.

It is possible to stop the execution of the test with Ctrl-C.
""")

    _utils.print_info("Press Ctrl-C to stop the test.")

    def print_time():
        """Print the current time."""
        _utils.print_info("Current time: %s" % time.strftime("%X
