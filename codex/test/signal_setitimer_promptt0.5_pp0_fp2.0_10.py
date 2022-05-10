import signal
# Test signal.setitimer(signal.ITIMER_REAL, 0, 1)

def handler(signum, frame):
    print('Alarm', signum)
    signal.setitimer(signal.ITIMER_REAL, 0, 1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0, 1)

while True:
    pass
