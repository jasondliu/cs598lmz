import signal
# Test signal.setitimer() with alarm
import sys
import time

def alarm_handler(signum, frame):
    print("alarm", time.time())
    print(signum, frame)
    signal.alarm(1)

signal.signal(signal.SIGALRM, alarm_handler)

signal.alarm(1)
print("alarm started")

while True:
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.2)
