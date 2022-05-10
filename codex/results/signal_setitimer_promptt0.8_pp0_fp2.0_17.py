import signal
# Test signal.setitimer
import time

def alarm_handler(signum, frame):
    print("SIGALRM")

signal.setitimer(signal.ITIMER_REAL, 0.5)
try:
    signal.signal(signal.SIGALRM, alarm_handler)
    time.sleep(1.0)
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    time.sleep(1.0)
print("OK")
