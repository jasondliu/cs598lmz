import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 2, 2)
signal.alarm(5); print('ok')
signal.pause(); print('nok')

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 2, 2)
signal.pause(); print('ok')

print('pending: ', signal.pending())
