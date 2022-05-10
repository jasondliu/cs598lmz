import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    print("Got signal", signum)
    raise SystemExit

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2)
print("Before the sleep")
signal.pause()
print("After the sleep")
