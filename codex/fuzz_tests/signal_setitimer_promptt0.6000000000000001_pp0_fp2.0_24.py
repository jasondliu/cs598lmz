import signal
# Test signal.setitimer
for i in [signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]:
    try:
        signal.setitimer(i, 2, 1)
        signal.setitimer(i, 0, 0)
    except RuntimeError:
        print("RuntimeError")

try:
    signal.setitimer(-1, 2, 1)
except ValueError:
    print("ValueError")
