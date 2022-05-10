import signal
# Test signal.setitimer

def handler(signum, frame):
    print("handler called")

# Create an alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# Wait for the alarm to go off
time.sleep(0.5)

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

print("after setitimer")
time.sleep(0.5)

# Create a periodic timer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(0.5)
print("after 0.5 seconds")
time.sleep(0.5)
print("after 1 second")
