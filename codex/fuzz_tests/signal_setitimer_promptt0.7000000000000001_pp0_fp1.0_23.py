import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
print(signal.getitimer(signal.ITIMER_REAL))
time.sleep(0.3)
print(signal.getitimer(signal.ITIMER_REAL))
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.3)
print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.setitimer for a signal
signal.alarm(4)
time.sleep(3)
signal.alarm(3)
time.sleep(3)
signal.alarm(0)

# Test signal.setitimer for a signal
print(signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1))
time.sleep(0.3)
print(signal.getitimer(signal.ITIMER_REAL))
