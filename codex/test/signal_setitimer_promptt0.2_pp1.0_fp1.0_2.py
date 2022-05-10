import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# Test signal.getitimer
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_VIRTUAL)
signal.getitimer(signal.ITIMER_PROF)

# Test signal.signal
signal.signal(signal.SIGALRM, lambda x,y: None)
signal.signal(signal.SIGVTALRM, lambda x,y: None)
signal.signal(signal.SIGPROF, lambda x,y: None)

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)
