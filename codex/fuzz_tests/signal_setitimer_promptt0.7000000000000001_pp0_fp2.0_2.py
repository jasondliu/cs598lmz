import signal
# Test signal.setitimer(), which is not supported on Windows.
try:
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0)
except Exception:
    print("SKIP")
    raise SystemExit

# Test signal.setitimer() with handler.
print("handling SIGALRM")

def handler(sig, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

# Test signal.setitimer() without handler.
print("not handling SIGALRM")
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

# Test signal.setitimer() with handler set to None.
print("not handling SIGALRM")
signal.signal(signal.SIGALRM, None)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

# Test signal.setitimer() with a one
