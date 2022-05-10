import signal
# Test signal.setitimer()

# This test is only valid on Linux and BSD systems, as Windows does
# not support setitimer()

if not hasattr(signal, 'setitimer'):
    raise ImportError('No setitimer() on this system')

import os
import sys
import time

def alarm_received(n, stack):
    print('ALARM!')

signal.signal(signal.SIGALRM, alarm_received)

# Schedule an alarm for 1 second in the future
signal.setitimer(signal.ITIMER_REAL, 1)

# This open() may hang indefinitely if the alarm signal is ignored
fd = os.open('/dev/tty', os.O_RDWR)

# Cancel the alarm
signal.setitimer(signal.ITIMER_REAL, 0)

os.write(fd, b'This is a test\n')

time.sleep(2)
os.close(fd)

# Verify that the alarm signal is delivered to a process which has
# nothing else to do but wait for the
