import signal
# Test signal.setitimer() and signal.setitimer()
#
# Test 1:
#  - setitimer() with ITIMER_REAL
#  - signal handler increments a counter
#  - check that counter is incremented at the expected rate
#
# Test 2:
#  - setitimer() with ITIMER_VIRTUAL
#  - signal handler increments a counter
#  - check that counter is incremented at the expected rate
#
# Test 3:
#  - setitimer() with ITIMER_PROF
#  - signal handler increments a counter
#  - check that counter is incremented at the expected rate
#
# Test 4:
#  - setitimer() with ITIMER_REAL
#  - signal handler increments a counter
#  - check that counter is incremented at the expected rate
#  - setitimer() with ITIMER_VIRTUAL
#  - signal handler increments a counter
#  - check that counter is incremented at the expected rate
#  - setitimer() with ITIMER_PROF
#  - signal handler increments a counter
#  -
