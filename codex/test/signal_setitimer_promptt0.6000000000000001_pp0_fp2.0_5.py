import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1, 0)

# Test signal.setitimer error conditions
try:
    signal.setitimer(-1, 1, 0)
except ValueError:
    pass
else:
    print("setitimer: no error for invalid signal number")
try:
    signal.setitimer(signal.ITIMER_REAL, "1", 0)
except TypeError:
    pass
else:
    print("setitimer: no error for invalid interval type")
try:
    signal.setitimer(signal.ITIMER_REAL, 1, "0")
except TypeError:
    pass
else:
    print("setitimer: no error for invalid interval type")

# Test signal.alarm
signal.alarm(1)

# Test signal.getitimer
time = signal.getitimer(signal.ITIMER_REAL)

# Test signal.getitimer error conditions
