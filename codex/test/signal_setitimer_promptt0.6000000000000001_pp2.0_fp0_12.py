import signal
# Test signal.setitimer() and signal.getitimer()
# These functions are not implemented in CPython,
# but is implemented in uPy

try:
    signal.setitimer
except AttributeError:
    print("SKIP")
    raise SystemExit

def alarm_handler(signum, frame):
    print("ALARM")
    raise SystemExit

signal.signal(signal.SIGALRM, alarm_handler)

# Set alarms
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.3, 0.3)

# Check alarms
print(signal.getitimer(signal.ITIMER_REAL))
print(signal.getitimer(signal.ITIMER_VIRTUAL))
print(signal.getitimer(signal.ITIMER_PROF))

# Wait for alarms
