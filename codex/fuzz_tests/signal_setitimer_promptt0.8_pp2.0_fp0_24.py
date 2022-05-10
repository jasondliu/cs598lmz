import signal
# Test signal.setitimer

def handler(signum, frame):
    print('Received', signum)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

import time, os
time.sleep(3)
pid = os.getpid()

print('Sending signal to', pid)
print(signal.getsignal(signal.SIGALRM))
os.kill(pid, signal.SIGALRM)

print('Done')

# Test signal.setitimer

def handler(signum, frame):
    print('Received', signum)
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

import time, os
time.sleep(3)
pid = os
