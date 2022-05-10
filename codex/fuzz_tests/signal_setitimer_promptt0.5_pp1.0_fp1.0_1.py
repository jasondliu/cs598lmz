import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1)
signal.setitimer(signal.ITIMER_PROF, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 1)

# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_PROF)
signal.getitimer(signal.ITIMER_VIRTUAL)

# Test signal.signal()
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.signal(signal.SIGVTALRM, signal.SIG_DFL)
signal.signal(signal.SIGPROF, signal.SIG_DFL)
signal.signal(signal.SIGCONT, signal.SIG_DFL)
signal.signal(signal.SIGSTOP, signal.SIG_DFL)
signal.sign
