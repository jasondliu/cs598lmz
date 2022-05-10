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

