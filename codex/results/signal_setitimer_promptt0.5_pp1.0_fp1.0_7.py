import signal
# Test signal.setitimer and signal.getitimer

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.1)
print(signal.getitimer(signal.ITIMER_REAL))

signal.setitimer(signal.ITIMER_VIRTUAL, 0.3, 0.2)
print(signal.getitimer(signal.ITIMER_VIRTUAL))

signal.setitimer(signal.ITIMER_PROF, 0.4, 0.3)
print(signal.getitimer(signal.ITIMER_PROF))

try:
    signal.setitimer(signal.ITIMER_MONOTONIC, 0.5, 0.4)
except AttributeError:
    print("signal.ITIMER_MONOTONIC not supported")
else:
    print(signal.getitimer(signal.ITIMER_MONOTONIC))

try:
    signal.setitimer(signal.ITIMER_REAL, 0.6
