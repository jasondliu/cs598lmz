import signal
# Test signal.setitimer() and signal.getitimer()

import sys
import time
import signal

signal.signal(signal.SIGALRM, lambda signum, frame: None)
signal.alarm(3)
time.sleep(0.5)

if sys.platform.startswith('sunos5'):
    signame = 'ITIMER_REAL'
elif sys.platform in ('darwin', 'freebsd6', 'freebsd7', 'freebsd8', 'freebsd9',
                      'freebsd10', 'freebsd11', 'netbsd5', 'openbsd5', 'linux'):
    signame = 'SIGALRM'
else:
    raise TestFailed("Don't know which signal to use")

signum = getattr(signal, signame)
signal.setitimer(signum, 1, 3)
time.sleep(0.5)
print('before:', signal.getitimer(signum))
time.sleep(1.5)
print('after :', signal.getitimer
