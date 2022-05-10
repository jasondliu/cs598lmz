import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print('Alarm')
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('Interrupted')
