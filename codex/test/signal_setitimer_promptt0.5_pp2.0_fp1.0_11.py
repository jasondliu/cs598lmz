import signal
# Test signal.setitimer

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

while True:
    pass
