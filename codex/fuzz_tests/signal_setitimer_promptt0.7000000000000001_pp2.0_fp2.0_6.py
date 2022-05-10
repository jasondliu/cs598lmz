import signal
# Test signal.setitimer and signal.itimer_value
# Test signal.setitimer and signal.itimer_gettime
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
time_real = signal.getitimer(signal.ITIMER_REAL)
time_real = signal.itimer_gettime(signal.ITIMER_REAL)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
time_virtual = signal.getitimer(signal.ITIMER_VIRTUAL)
time_virtual = signal.itimer_gettime(signal.ITIMER_VIRTUAL)
# Test signal.setitimer and signal.itimer_value
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.2)
time_prof = signal.getitimer(signal.ITIMER_PROF)
time_prof = signal.itimer_gettime(signal.ITIMER_PROF)

# Test
