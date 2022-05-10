import selectors
import sys
import time
import types

#-------------------------------------------------------------------------------

class _EventTimer:

    # This class represents an event timer.
    # The timer is started when the constructor is called.
    # The timer is stopped when the 'stop' method is called.
    # The duration of the timer is returned in milliseconds when
    # the 'duration' method is called.

    def __init__(self):
        self._start_time = time.time()

    def stop(self):
        self._stop_time = time.time()

    def duration(self):
        return (self._stop_time - self._start_time) * 1000

#-------------------------------------------------------------------------------

def _main():

    # This is the main function that runs the tests.
    # A number of tests are performed.
    # For each test, a report string is printed.
    # After all the tests have been done a final report will be printed.
    # The final report contains the number of tests that succeeded,
    # the number of tests that failed and the time it took to perform all
    # the tests.

    # Def
