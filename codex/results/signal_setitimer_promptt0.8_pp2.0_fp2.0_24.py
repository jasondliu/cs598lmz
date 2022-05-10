import signal
# Test signal.setitimer(), and the ITIMER_REAL timer in particular.
import sys
import time
# Import thread so that we can use thread.start_new_thread().
import thread
# Test thread.interrupt_main().
import unittest

verbose = 0

# Return the amount of time to delay for alarm() tests.
def alarm_delay():
    return 0.1

# Return the amount of time to delay for setitimer() tests.
def itimer_delay():
    return 0.1

def thread_sleep(duration):
    # Just like time.sleep(), but delays for a thread and not the whole
    # process.
    old_handler = signal.signal(signal.SIGALRM, lambda signum, frame: None)
    old_alarm = signal.alarm(duration)
    # Ignore EINTR while waiting for the alarm to go off.
    while True:
        try:
            time.sleep(999999999)
        except IOError, (errno, strerror):
            if errno != errno.EINTR:
                raise IO
