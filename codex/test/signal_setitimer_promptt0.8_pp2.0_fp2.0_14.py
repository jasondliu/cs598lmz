import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 1.5)
print('sleep')
time.sleep(2)
print('yo')
