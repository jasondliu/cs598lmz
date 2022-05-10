import signal
# Test signal.setitimer()
# This code uses the "signal" module to setup a handler for SIGALRM
# and prints a message  whenever the signal is received

def handler(signum, frame):
    #signal.setitimer(signal.ITIMER_REAL, 0)
    print('SIGALRM received')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)  # Send SIGALRM after 5s

while True:
    print('Waiting...')
    time.sleep(3)
 
 

import signal
import time

# Define signal handler function
def myHandler(signum, frame):
    print("Now, it's the time")
    exit()

# register signal.SIGALRM's handler 
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(8)
# This will never be executed
while True:
    print('not yet')
    time.sleep(2)
 
 
