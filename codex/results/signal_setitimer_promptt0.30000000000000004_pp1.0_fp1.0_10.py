import signal
# Test signal.setitimer() and signal.getitimer()

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.1)
print(signal.getitimer(signal.ITIMER_REAL))

signal.setitimer(signal.ITIMER_VIRTUAL, 0.3, 0.2)
print(signal.getitimer(signal.ITIMER_VIRTUAL))

signal.setitimer(signal.ITIMER_PROF, 0.4, 0.3)
print(signal.getitimer(signal.ITIMER_PROF))

# Test signal.setitimer() with a negative value
try:
    signal.setitimer(signal.ITIMER_REAL, -1, 0.1)
except ValueError:
    print("ValueError")

# Test signal.setitimer() with a negative value
try:
    signal.setitimer(signal.ITIMER_REAL, 0.1, -1)
except ValueError:
    print("
