import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
print(signal.itimer_gettime(signal.ITIMER_VIRTUAL))
print(signal.itimer_gettime(signal.ITIMER_VIRTUAL))
print(signal.itimer_gettime(signal.ITIMER_PROF))
print(signal.itimer_gettime(signal.ITIMER_PROF))
