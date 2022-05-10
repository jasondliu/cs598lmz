import signal
# Test signal.setitimer()
def signal_handler(signum, frame):
    print("setitimer() works")
    sys.exit(0)

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
while True:
    pass
