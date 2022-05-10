import signal
# Test signal.setitimer()

def handler(sig, frame):
    print("Got signal", sig)
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    pass
