import signal
# Test signal.setitimer() and signal.getitimer()

# We need to set the handler for SIGALRM to something
# other than SIG_DFL, otherwise the alarm() call will
# kill the process.
def alarm_handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, alarm_handler)

# We set an alarm for 1 second, wait for 2 seconds,
# and then check how much time remains.
signal.setitimer(signal.ITIMER_REAL, 1, 0)
time.sleep(2)
remaining = signal.getitimer(signal.ITIMER_REAL)
print("Remaining time:", remaining)

# Now we cancel the alarm.
signal.setitimer(signal.ITIMER_REAL, 0, 0)
time.sleep(2)
remaining = signal.getitimer(signal.ITIMER_REAL)
print("Remaining time:", remaining)
