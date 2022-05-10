import signal
# Test signal.setitimer(), signal.getitimer()

# test setitimer
print('Test setitimer()')
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# test setitimer error
print('Test setitimer() invalid argument')
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
except TypeError:
    print('TypeError')
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 'a')
except TypeError:
    print('TypeError')
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 'a')
except TypeError:
    print('TypeError')
