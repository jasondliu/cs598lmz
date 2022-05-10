import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.05, 0.05)
signal.alarm(5)

while True:
    time.sleep(2)

print("Returned from loop")
"""
