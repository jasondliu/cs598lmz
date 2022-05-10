import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

# Test signal.signal
def handler(signum, frame):
    print(signum, frame)

signal.signal(signal.SIGUSR1, handler)

# Test signal.getsignal
print(signal.getsignal(signal.SIGUSR1))

# Test signal.getitimer
print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.pause
signal.pause()
