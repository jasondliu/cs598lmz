import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, interval, interval)
# Expects SIGVTALRM to be sent at specified intervals

# BUG: How to test on a system without POSIX timers?

class AlarmException(Exception):
    pass

def alarm_handler(signum, frame):
    raise AlarmException

def nonposix_test():
    global interval
    interval = 1
    signal.signal(signal.SIGVTALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_VIRTUAL, interval, interval)
