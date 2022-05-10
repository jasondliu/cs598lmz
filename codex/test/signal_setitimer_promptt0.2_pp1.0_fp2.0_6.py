import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print('Alarm', signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

while True:
    print('Tick')
