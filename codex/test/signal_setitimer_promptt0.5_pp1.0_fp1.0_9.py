import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Test signal.setitimer with arguments of wrong type
try:
    signal.setitimer(signal.ITIMER_REAL, '0.1', 0.1)
except TypeError:
    pass
else:
    print("setitimer(ITIMER_REAL, '0.1', 0.1) should have raised TypeError")
try:
    signal.setitimer(signal.ITIMER_REAL, 0.1, '0.1')
except TypeError:
    pass
else:
    print("setitimer(ITIMER_REAL, 0.1, '0.1') should have raised TypeError")

# Test signal.setitimer with invalid arguments
