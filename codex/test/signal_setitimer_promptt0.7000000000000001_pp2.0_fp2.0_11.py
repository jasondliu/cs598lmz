import signal
# Test signal.setitimer and signal.getitimer

sigs = signal.getsignal(signal.SIGALRM)
print(sigs)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
# signal.setitimer(signal.ITIMER_REAL, 0.1)
print(signal.getitimer(signal.ITIMER_REAL))

def handler(signum, frame):
    print("handler")
    signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

signal.signal(signal.SIGALRM, handler)

# signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

