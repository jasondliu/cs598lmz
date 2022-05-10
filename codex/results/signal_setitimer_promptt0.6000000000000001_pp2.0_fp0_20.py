import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

import sys
import time

print('START:', time.ctime())
time.sleep(2)
print('DONE :', time.ctime())

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)

import sys
import time

print('START:', time.ctime())
time.sleep(2)
print('DONE :', time.ctime())

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.1, 0)

import sys
import time

print('START:', time.ctime
