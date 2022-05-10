import signal
# Test signal.setitimer to send SIGALARM
import time

def handler(num, frame):
    print("Received", num)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    time.sleep(1)
