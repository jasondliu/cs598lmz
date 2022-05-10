import signal
# Test signal.setitimer

def handler(signum, frame):
    print(signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)

time.sleep(2)
