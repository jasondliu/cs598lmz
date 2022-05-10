import signal
# Test signal.setitimer() and signal.alarm() (which are different).

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)

