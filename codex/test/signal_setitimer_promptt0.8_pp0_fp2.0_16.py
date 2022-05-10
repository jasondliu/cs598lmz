import signal
# Test signal.setitimer() and signal.getitimer()

# ITIMER_REAL decrements in real time, and delivers SIGALRM upon expiration
signal.setitimer(signal.ITIMER_REAL, 3.2)
time.sleep(1.1)
