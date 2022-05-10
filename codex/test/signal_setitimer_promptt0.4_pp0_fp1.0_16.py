import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # Disable the alarm

print('Continuing...')

#!/usr/bin/env python
# encoding: utf-8

import os
import signal

def receive_signal(signum, stack):
    print('Received:', signum)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)

