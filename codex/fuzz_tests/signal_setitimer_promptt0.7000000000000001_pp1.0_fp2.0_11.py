import signal
# Test signal.setitimer()
#
# Note: this test uses the os.kill() function, which is not available on
# all platforms.
import os, sys
import time

def alarm_handler(signum, frame):
    global alarm_fired
    alarm_fired = 1
    print("Alarm handler:", signum, frame)

def child():
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    print(signal.setitimer(signal.ITIMER_REAL, 10.0, 5.0))
    signal.pause()

def parent():
    # This test will only work if the timer isn't already running in the
    # child.  The first call to setitimer() in the child will disable
    # the timer in the parent.  So if the parent has already started
    # running the timer this test will fail.
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 30.0, 0.0)
    pid = os.
