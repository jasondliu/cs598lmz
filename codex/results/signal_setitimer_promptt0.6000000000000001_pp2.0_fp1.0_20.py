import signal
# Test signal.setitimer() in a simple way

def handler(signum, frame):
    print('Alarm')

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)

while True:
    pass

# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
# ^C
# Alarm
