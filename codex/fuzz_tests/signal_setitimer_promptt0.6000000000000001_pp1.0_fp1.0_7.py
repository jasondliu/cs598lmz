import signal
# Test signal.setitimer()

def _alarm_handler(signum, frame):
    print "*** _alarm_handler: got signal", signum, "***"

signal.signal(signal.SIGALRM, _alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0, 1)
time.sleep(3)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.setitimer() with a handler that raises an exception

def _alarm_handler_raise(signum, frame):
    print "*** _alarm_handler_raise: got signal", signum, "***"
    raise ValueError, "error from _alarm_handler_raise"

signal.signal(signal.SIGALRM, _alarm_handler_raise)

signal.setitimer(signal.ITIMER_REAL, 0, 1)
try:
    time.sleep(3)
except ValueError, e:
    print "*** Caught exception:",
