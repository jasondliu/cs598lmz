import signal
# Test signal.setitimer by setting it once then calling signal.pause.
# It should raise a KeyboardInterrupt.
signal.setitimer(signal.ITIMER_REAL, 1, 0)
try:
    signal.pause()
except KeyboardInterrupt:
    pass

sys.exit(0)
