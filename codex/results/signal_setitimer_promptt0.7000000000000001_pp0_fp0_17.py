import signal
# Test signal.setitimer(signal.ITIMER_PROF, 1, 0.2)
signal.setitimer(signal.ITIMER_PROF, 1, 0.2)

def handler(signum, frame):
    print("catch it")

signal.signal(signal.SIGPROF, handler)
while True:
    time.sleep(1)
	
'''

'''
# Test signal.setitimer(signal.ITIMER_REAL, 1, 0.2)
import signal
import time

def handler(signum, frame):
    print("catch it")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0.2)
while True:
    time.sleep(1)
'''

'''
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0.2)
import signal
import time

def handler(signum, frame):
    print("catch it")

