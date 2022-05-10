import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print("Got alarm")

signal.signal(signal.SIGALRM, alarm_handler)

# Set an alarm
signal.setitimer(signal.ITIMER_REAL, 0.2)

# Do some busy work
t = time.time()
while time.time() < t + 1:
    pass

# There should be exactly one alarm
print(signal.getitimer(signal.ITIMER_REAL))
