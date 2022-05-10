import signal
# Test signal.setitimer
# Does not work on Windows

# Python function to illustrate
# use of signal.setitimer() method
import os
import signal
import sys,time
 
# signal handler
def signal_handler(sig, frame):
    print("Inside signal handler!")
    time.sleep(1)
 
# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, signal_handler)
 
# signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 2, 0.5)
 
while True:
    time.sleep(1)
    print("Waiting....")

# signal.setitimer(signal.ITIMER_REAL, 2, 0.5)
