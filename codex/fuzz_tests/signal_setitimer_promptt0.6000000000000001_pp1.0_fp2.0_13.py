import signal
# Test signal.setitimer()

# Set a handler for SIGALRM
def handler(signum, frame):
    print("Received SIGALRM")

signal.signal(signal.SIGALRM, handler)

# Set an alarm for 1 second
signal.setitimer(signal.ITIMER_REAL, 1)

# Wait for the alarm
print("Sleeping for 2 seconds")
time.sleep(2)

# Disable the alarm
print("Disabling the alarm")
signal.setitimer(signal.ITIMER_REAL, 0)
