import signal
# Test signal.setitimer for base or realtime clock.
# Contributed by Daniel Hyams dhyams at gmail.com
# 2 Feb 2004
#
import os
import signal
import subprocess
import sys
import threading

def starter():
    # given the time between interupts is at most a few microseconds
    # we need to start the timing threads very soon after the main thread
    # is started by the subprocess spawned by the parent process to
    # avoid race conditions.
    #
    # ergo, THIS FUNCTION must be started as a separate thread with
    # the thread starting _immediately_ after the process is spawned by
    # the parent process.
    #
    # if you want to run on realtime clocks, os.times() doesn't give
    # enough resolution on many platforms. using time.time() instead
    # gives much better resolution. it's also a lot cheaper than os.times().
    import time
    if sys.argv[1] == 'realtime':
        t0 = time.time()
    else:
        t0 = os.times()[4]

    t1
