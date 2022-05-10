import signal
# Test signal.setitimer
val = signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
print val
