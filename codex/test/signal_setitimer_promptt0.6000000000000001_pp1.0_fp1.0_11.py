import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the timer to go off in 2 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# Do stuff
while True:
    print('Working...')

# Press Ctrl+C to end the program
import signal
import os

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    print('Sleeping...')
    time.sleep(2)
    print('Exiting...')
    os._exit(1)

signal.signal(signal.SIGINT, handler)

while True:
    print('Working...')
    time.sleep(1)

# Use Ctrl+Z to suspend the program
# Then use kill -INT pid to end the program

import signal
import os

def handler(signum, frame):
    print('Signal handler called with signal', signum)
   
