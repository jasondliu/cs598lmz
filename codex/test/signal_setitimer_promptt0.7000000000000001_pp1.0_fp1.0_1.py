import signal
# Test signal.setitimer call
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# See if the signal is handled
print('Test of SIGALRM:', signal.getsignal(signal.SIGALRM))

# Test signal.setitimer call
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# See if the signal is handled
print('Test of SIGALRM:', signal.getsignal(signal.SIGALRM))

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# See if the signal is handled
print('Test of SIGALRM:', signal.getsignal(signal.SIGALRM))

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# See if the signal is handled
print('Test of SIGALRM:', signal.getsignal(signal.SIGALRM))

