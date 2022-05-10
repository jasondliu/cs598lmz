import signal
# Test signal.setitimer on Windows
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
print("OK")
