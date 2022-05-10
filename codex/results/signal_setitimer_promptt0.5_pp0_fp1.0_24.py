import signal
# Test signal.setitimer()

def handler(sig, frame):
    print("Signal", sig)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for the alarm
time.sleep(5)
