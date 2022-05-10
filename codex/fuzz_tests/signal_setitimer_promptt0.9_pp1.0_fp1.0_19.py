import signal
# Test signal.setitimer with signal.alarm

import os

print("begin test with signal.alarm...")

def alarm_handler(*args):
    print("alarm signal has been received")
    raise AssertionError("alarm signal received but no alarm set")
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)
signal.pause()

print("begin test with os.kill...")
os.kill(os.getpid(), signal.SIGALRM)
signal.pause()
