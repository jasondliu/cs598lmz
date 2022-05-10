import signal
# Test signal.setitimer() and signal.getitimer()
import os
import time

def handler(signum, frame):
    print("Alarm", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2, 1)

print("Before sleep")
time.sleep(5)
print("After sleep")

print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.setitimer() and signal.getitimer()
import os
import time

def handler(signum, frame):
    print("Alarm", signum)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2, 1)

print("Before sleep")
time.sleep(5)
print("After sleep")

print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.setitimer() and signal.getit
