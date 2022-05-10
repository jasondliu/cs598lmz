import signal
# Test signal.setitimer
import time, os

def check_alarm(signum, expected):
    assert signum == signal.SIGALRM
    assert signal.getitimer(signal.ITIMER_REAL) == expected

signal.signal(signal.SIGALRM, check_alarm)

signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_REAL, 0, 0.2)
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
time.sleep(0.1)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
