import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass

# Output:
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Alarm
# Al
