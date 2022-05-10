import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.4)
print('Sleeping\n')
time.sleep(1.1)

# Test signal.getitimer
print('Timer:', signal.getitimer(signal.ITIMER_REAL))
