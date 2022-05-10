import signal
# Test signal.setitimer() with SIGALRM.
signal.setitimer(signal.ITIMER_REAL, 0.005, 0)
signal.signal(signal.SIGALRM, lambda signum, itimerval: setattr(signal, 'alarm_received', True))
signal.alarm_received = False
