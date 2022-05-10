import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass

# Output:
# Alarm
# Alarm
# Alarm
# Alarm
# ...

# The timer is not reset when the signal handler is called.
# So the timer will expire again after 0.1 seconds.
# This is the same behavior as the Unix alarm() function.
