import signal
# Test signal.setitimer
print signal.setitimer(signal.ITIMER_REAL, 1.0)
print signal.setitimer(signal.ITIMER_REAL, 0.0)
print signal.setitimer(signal.ITIMER_REAL, 0.0, 0.0)
# Test signal.getitimer
print signal.getitimer(signal.ITIMER_REAL)
print signal.getitimer(signal.ITIMER_REAL)
print signal.getitimer(signal.ITIMER_REAL)

# Test signal.setitimer with invalid input
try:
    signal.setitimer(signal.ITIMER_REAL, 2)
except TypeError:
    print 'TypeError'
try:
    signal.setitimer(signal.ITIMER_REAL, 1, 2)
except TypeError:
    print 'TypeError'
