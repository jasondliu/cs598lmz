import select
# Test select.select()
#
# It seems that select.select() is not interrupted by signals. It will
# be interrupted by a signal only when it is waiting for data.
#
# The select.select() call should be in a try/except clause to catch
# the EINTR signal. The signal handler should set a flag to indicate
# that the signal has been caught and the select.select() call should
# be repeated.
#
# The documentation for select.select() says that it "is not a
# restartable system call". That statement is not true. A signal
# causes EINTR to be returned. The select.select() call can be
# repeated until it does not return EINTR.

import signal
import os
import time

# The flag to indicate that a signal has been caught.
signal_caught = False

def signal_handler(signal, frame):
    "The signal handler."
    global signal_caught
    signal_caught = True

# Register the signal handler.
signal.signal(signal.SIGINT, signal_handler)

loop_count = 0
