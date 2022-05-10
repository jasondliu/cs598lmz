import signal
# Test signal.setitimer()

def alarm_handler(signal, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

print('Before:', signal.getitimer(signal.ITIMER_REAL))
signal.pause()
print('After:', signal.getitimer(signal.ITIMER_REAL))

# Test SIGIO

def io_handler(signal, frame):
    print('SIGIO!')

signal.signal(signal.SIGIO, io_handler)

import os
# assume stdin is non-blocking
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETOWN, os.getpid())
