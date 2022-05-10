import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Received signal", signum, "in frame", frame)
    raise SystemExit("Done")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# Wait for the signal
