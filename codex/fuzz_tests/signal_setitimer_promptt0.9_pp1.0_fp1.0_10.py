import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 1.0)
assert(signal.getitimer(signal.ITIMER_REAL)[0] == 0.1 and
       signal.alarm(0) == 0)
# Test signal.getitimer
signal.alarm(10)
assert(signal.getitimer(signal.ITIMER_REAL)[0] == 10 and
       signal.alarm(0) == 10)
# Test signal.itimer_gettime
signal.alarm(10)
assert(signal.itimer_gettime(signal.ITIMER_REAL)[0] == 10 and
       signal.alarm(0) == 10)
# Test signal.alarm
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.alarm(10)
assert(signal.getitimer(signal.ITIMER_REAL)[0] == 10 and
       signal.alarm(0) == 10)
# Test signal
