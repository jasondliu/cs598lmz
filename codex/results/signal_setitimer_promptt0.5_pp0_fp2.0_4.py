import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
