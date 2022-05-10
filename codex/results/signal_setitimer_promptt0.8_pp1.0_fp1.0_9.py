import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1)
signal.pause()
# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
# Test signal.setitimer with SIG_DFL
signal.setitimer(signal.ITIMER_REAL, 1, SIG_DFL)
signal.pause()

# Check that SIG_DFL and SIG_IGN are defined
signal.SIG_IGN
signal.SIG_DFL

print("ok")
