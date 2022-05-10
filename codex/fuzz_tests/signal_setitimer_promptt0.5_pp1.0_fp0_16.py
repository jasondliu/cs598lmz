import signal
# Test signal.setitimer()
# The interval is given in seconds, the default is 0.0 seconds
signal.setitimer(signal.ITIMER_REAL, 0.2)
signal.pause()

# Test signal.getitimer()
print("Timer:", signal.getitimer(signal.ITIMER_REAL))
