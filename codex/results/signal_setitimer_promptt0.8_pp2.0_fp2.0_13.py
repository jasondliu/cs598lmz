import signal
# Test signal.setitimer() and signal.getitimer()

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)

# Schedule an alarm for 1 second in the future.
signal.setitimer(signal.ITIMER_REAL, 1)

try:
    print('Before:', signal.getitimer(signal.ITIMER_REAL))
    signal.pause()
except Alarm:
    print('Alarm')

print('After:', signal.getitimer(signal.ITIMER_REAL))

# Disable the alarm.
signal.setitimer(signal.ITIMER_REAL, 0)

print('Disabled:', signal.getitimer(signal.ITIMER_REAL))

# Schedule an alarm for 1 second in the future.
signal.setitimer(signal.ITIMER_REAL, 1)

try:
    print('Before:', signal.getit
