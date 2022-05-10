import select
# Test select.select() using a non-blocking pair of pipe file descriptors.
import os
import sys
import struct
import time
import threading

# Number of seconds to run the test
RUN_TIME = 10

# The code

def read(start_events, stop_events, rpipe, expect):
    # Make the pipe non-blocking
    fd = rpipe.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    # Loop until 'expect' events have been seen.
    start_events.wait(RUN_TIME)
    end_time = time.time() + RUN_TIME
    expect_events = expect
    seen_events = 0
    time.sleep(0.1)
