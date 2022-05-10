import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0) and signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
# in a tight loop.
# Apart from the very first signal, it should not raise EINTR.

def handler(signum, frame):
    print("alarm")

signal.signal(signal.SIGALRM, handler)
try:
    for _ in range(100):
        signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
        time.sleep(0.01)
except OSError:
    raise
