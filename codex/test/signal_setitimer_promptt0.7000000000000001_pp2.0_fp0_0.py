import signal
# Test signal.setitimer()
class Alarm(Exception):
    pass
def alarm_handler(signum, frame):
    raise Alarm
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)    # Schedule the first alarm for 0.1 seconds
