import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, None)
# Expected Output:
# >>>
#
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
# Expected Output:
# >>>
#
# Test signal.setitimer
signal.setitimer(signal.ITIMER_PROF, 0.1, 1)
# Expected Output:
# >>>
#
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
# Expected Output:
# >>>
#
# Test signal.setitimer
try:
    signal.setitimer(-1, 0.1, 0.2)
except ValueError:
    tprint("ValueError")
# Expected Output:
# ValueError
# >>>
#
# Test signal.setitimer
try:
    signal.setitimer(4, 0.1, 0.2)

