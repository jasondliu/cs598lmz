import signal
# Test signal.setitimer()
def handler(n, frame):
    print("Got SIGALRM")
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2, 0)
signal.pause()
