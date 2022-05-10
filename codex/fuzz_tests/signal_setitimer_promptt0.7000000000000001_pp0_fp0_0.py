import signal
# Test signal.setitimer() to ensure that SIGALRM is being delivered.
$ cat sigtest.py
import signal

def handler(sig, frame):
    print("SIGALRM received")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)
while True:
    pass
$ ./python -u sigtest.py
...
SIGALRM received
SIGALRM received
SIGALRM received
^CTraceback (most recent call last):
  File "sigtest.py", line 9, in <module>
    while True:
KeyboardInterrupt
$
"""

import signal
import sys
import time

#
# Define a function to be used as a signal handler.
#
def handler(signum, frame):
    for n in range(2):
        sys.stdout.write('SIGALRM received\n')
        sys.stdout.flush()
        time.sleep(0.5)

#
# Register our signal handler.
#
sign
