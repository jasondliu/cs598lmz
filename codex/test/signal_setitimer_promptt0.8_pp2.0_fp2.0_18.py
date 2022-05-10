import signal
# Test signal.setitimer
import sys

def alarm_received(n, stack):
    print("Alarm", n)

signal.signal(signal.SIGALRM, alarm_received)

# Defaults
if sys.platform == "win32":
    print("Note: setting ITIMER_REAL timeout to 0.1 seconds")
    signal.setitimer(signal.ITIMER_REAL, 0.1)
else:
    print("Note: setting ITIMER_REAL timeout to 1.1 seconds")
    signal.setitimer(signal.ITIMER_REAL, 1.1)
print("before")
sys.stdout.flush()
signal.pause()
print("after 1st pause()")
sys.stdout.flush()
signal.pause()
print("after 2nd pause()")
sys.stdout.flush()

# 0.5 seconds
signal.setitimer(signal.ITIMER_REAL, 0.5)
print("before")
sys.stdout.flush()
signal.pause()
