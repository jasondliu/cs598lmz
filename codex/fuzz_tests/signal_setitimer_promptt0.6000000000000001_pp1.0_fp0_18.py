import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 1)
print("alarm set")
# signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(3)
print("alarm disabled")
time.sleep(3)
print("alarm enabled")
signal.setitimer(signal.ITIMER_REAL, 1, 1)
time.sleep(3)
print("alarm disabled")

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 1)
print("alarm set")
signal.setitimer(signal.ITIMER_REAL, 0)
time.sleep(3)
print("alarm disabled")
time.sleep(3)
print("alarm enabled")
signal.setitimer(signal.ITIMER_REAL, 1, 1)
time.sleep(3)
print("alarm disabled")

# Test signal.setitimer() with 0
signal.setitimer
