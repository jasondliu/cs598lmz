import signal
# Test signal.setitimer(), signal.pause(), signal.setitimer().

def alarm_handler(signum, frame):
    print "hello"

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 3.0)
signal.pause()
