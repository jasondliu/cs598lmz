import signal
# Test signal.setitimer()
# set the timer to 5 seconds, the call the alarm handler after 5 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

