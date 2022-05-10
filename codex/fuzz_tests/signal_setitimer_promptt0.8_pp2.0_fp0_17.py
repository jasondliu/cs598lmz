import signal
# Test signal.setitimer() function

def handler(signum, frame):
    print('Got signal', signum)
    print('itimer seconds left is', signal.setitimer(signal.ITIMER_REAL, 0))
    signal.alarm(1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 1)

while True:
    time.sleep(0.1)
    print('still in main')
