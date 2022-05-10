import signal
# Test signal.setitimer by setting an alarm and waiting for it to go off.

def handler(signum, frame):
    global got_alarm
    got_alarm = True

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

got_alarm = False
while not got_alarm:
    pass

