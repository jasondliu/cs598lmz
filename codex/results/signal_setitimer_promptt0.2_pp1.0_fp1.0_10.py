import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    pass
